

function rutaGrafo = dijkstra1(grafo, Inicio, Fin)
% Se asigna memoria.
rutaGrafo = cell(numel(Inicio), numel(Fin));
distanciaMinima = zeros(numel(Inicio), numel(Fin));

%Matrices con ceros e in
saltos = min(size(grafo));
PorVisitar = zeros(saltos, 1);
visitados = inf(saltos, 1);

for i = 1:numel(Inicio)
    
    % Inicializamos las matrices.
    posicion = Inicio(i);
    if issparse(grafo) %  returna valor logico 1 (true) si la clase es escasa y logico 0 (false) otro caso.
        index = transpose(full(grafo(posicion, :) > 0.0)); %devuelve la transpuesta no conjugada, esto es, intercambia el índice de fila y columna de cada elemento
        index(posicion) = true;
    else
        index = transpose(not(isinf(grafo(posicion, :)))); %devuelve una matriz del mismo tamaño que contiene 1s lógicos 1 (verdadero) donde los elementos de A son infinitos y 0 lógico (falso) donde no lo son.
    end
    visitados(:) = inf; %Se crea matriz de infinitos
    visitados(index) = transpose(grafo(posicion, index)); %Intercambia indice de fila y columna 
    PorVisitar(:) = 0;
    PorVisitar(index) = posicion; %Se va actualizando dependiendo la posiciòn
    fila = find(index);
    
    % Recorrer nodos dentro del grafo.
    while not(isempty(fila)) % Devuelve un 1 lógico (verdadero) si está vacío y un 0 lógico (falso) en caso contrario. 
        nodoInicio = fila(1);
        distance = transpose(visitados(nodoInicio) + grafo(nodoInicio, :));
        index = distance < visitados;
        if issparse(grafo)
            index = and(index, full(transpose(grafo(nodoInicio, :) > 0)));
        end
        if any(index) %si es distinto de cero
            visitados(index) = distance(index);
            PorVisitar(index) = nodoInicio;
            fila = cat(1, fila(2:end, :), find(index));
        else
            fila = fila(2:end, :);
        end
    end
    
    % Almacenar los nodos por los que ha pasado.
    for j = 1:numel(Fin)
        rutaGrafo{i, j} = zeros(size(PorVisitar));
        nodoFin = Fin(j);
        for nodoInicio = numel(PorVisitar):(-1):1
            if or(eq(posicion, nodoFin), eq(nodoFin, 0))
                break
            end
            rutaGrafo{i, j}(nodoInicio) = nodoFin;
            nodoFin = PorVisitar(nodoFin);
        end
        if eq(posicion, nodoFin)
            rutaGrafo{i, j}(nodoInicio) = nodoFin;
            rutaGrafo{i, j} = rutaGrafo{i, j}(nodoInicio:end);
        else
            rutaGrafo{i, j} = [];
        end
    end
    distanciaMinima(i, :) = visitados(Fin);
    disp("Distancia mínima: "+distanciaMinima);
 
end


