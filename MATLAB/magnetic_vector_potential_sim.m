%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Name: Barry Cimring
% Date: August 10, 2020
% Description: This is a magnetic potential field simulator. 
%              If a current density, j(x, y, z), is specified 
%              (in 3 dimensions) the resulting vector potential, 
%              A(x, y, z), is calculated and plotted on a 3D quiver vector 
%              plot. This plot displays the magnitude of the vector 
%              potential proportional to the displayed vector. 
%
%              The example below displays a current loop centred in the
%              finite element mesh and the resulting vector potential. 
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% dimension of simulation
d = 10;  

% max is 31^3
N = d^3; 

% distance between mesh elements
h = 1;   

% matrix describing linearized differential 2nd order differential equation
mat_A = diag( 6*ones(N, 1) ); 

% populate PDE equation inverse
for i = 1:N
    
    % has a point to the left
    if ( mod(i,d) ~= 1 )
        mat_A( N*(i-2) + i ) = -1;
    end
    
    % has a point to the right
    if ( mod(i,d) ~= 0 ) && (  N*i + i < N^2 )
        mat_A( N*i + i ) = -1;
    end

    % has a point behind
    if ( i > d^2 + 1 )
        mat_A( round(N*(i-1) + i - N^(5/3), 0) ) = -1;
    end
    
    % has a point in front
    if ( i < (N - d^2 + 1 ))
        mat_A( round(N*(i-1) + i + N^(5/3), 0) ) = -1;
    end
    
    % has a point above
    if ( mod( i, d^2 ) >= d + 1 ) || ( mod( i, d^2 ) == 0 )
        mat_A( round(N*(i) + i - N*(d + 1))) = -1;
    end
    
    % has point below 
    if ( mod( i, d^2 ) <= d^2 - d + 1 ) && ( mod( i, d^2 ) ~= 0 ) && ( round(N*(i-1) + i + N*d) < N*N)
        mat_A(  round(N*(i-1) + i + N*d) ) = -1;
    end
    
end

% current loop input
j1 = zeros( N, 1);
j1(round((N + d^2 + d + 1)/2)) = 5;
j1(round((N + d^2 + d + 3)/2)) = -5;
j1(round((N + d^2 - d + 3)/2)) = -5;
j1(round((N + d^2 - d + 1)/2)) = 5;
j2 = zeros( N, 1);
j2(round((N + d^2 + d + 1)/2)) = 5;
j2(round((N + d^2 + d + 3)/2)) = 5;
j2(round((N + d^2 - d + 3)/2)) = -5;
j2(round((N + d^2 - d + 1)/2)) = -5;
j3 = zeros( N, 1);

% three components of inverse matrix
A1 = h^2*inv(mat_A)*j1;
A2 = h^2*inv(mat_A)*j2;
A3 = h^2*inv(mat_A)*j3;


% Create position arrays for data points        %
y = transpose(0:1:(d-1));
for i = 1:d^2-1
    y = [y; transpose(0:1:(d-1))];
end
y = y*h;

x = zeros( d^2 , 1);
for i = 1:d-1
    x = [x; h*i*ones( d^2 , 1)];
end

z0 = (d-1)*ones(d, 1);
for i = 1:(d-1)
    z0 = [z0; (d - 1 - i)*ones(d, 1)];
end

z = z0;
for i = 2:(d)
    z = [z; z0];
end
z = z*h;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Below is for visualization purposes
% starting points for streamlines
startx = -0:h:h*d;
starty = -0:h:h*d;
startz = -0:h:h*d;

% convert to 3D array for streamline plot
A1_3D = zeros( d, d, d );
for i = 1:d
    for j = 1:d
        A1_3D( i, : , j ) = A1(1 + (j - 1)*d^2 + (i - 1)*d : (j - 1)*d^2 + i*d);
    end
end

% convert to 3D array for streamline plot
A2_3D = zeros( d, d, d );
for i = 1:d
    for j = 1:d
        A2_3D( i, : , j ) = A2(1 + (j - 1)*d^2 + (i - 1)*d : (j - 1)*d^2 + i*d);
    end
end

% convert to 3D array for streamline plot
A3_3D = zeros( d, d, d );
for i = 1:d
    for j = 1:d
        A3_3D( i, : , j ) = A3(1 + (j - 1)*d^2 + (i - 1)*d : (j - 1)*d^2 + i*d);
    end
end

% 3D x, y, z arrays
x_3D = zeros( d, d, d);
y_3D = x_3D;
z_3D = x_3D;

for i = 1:d
    x_3D(i, :, :) =  (i-1)*h*ones(d, d);
end

for i = 1:d
    y_3D(:, i, :) =  (i-1)*h*ones(d, d);
end

for i = 1:d
    z_3D(:, :, i) =  (i-1)*h*ones(d, d);
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

quiver3(x_3D, y_3D, z_3D, A1_3D, A2_3D, A3_3D)
xlabel('x')
ylabel('y')
zlabel('z')

%streamline(x_3D, y_3D, A1_3D, A2_3D, 0:1:3, zeros(size(0:1:3)) )

%scatter3(x, y, z, A1, 'filled', C)