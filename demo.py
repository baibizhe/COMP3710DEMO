import torch
import matplotlib.pyplot as plt
####
def vicsek_fractal(iterations):
    # Initialize the matrix to be a 3x3 tensor
    matrix = torch.tensor([[1., 0., 1.], 
                           [0., 1., 0.], 
                           [1., 0., 1.]])

    for _ in range(iterations - 1):
        # Determine the current size of the matrix
        s = matrix.shape[0]
        
        # Expand the current matrix by creating a larger one filled with zeros
        new_matrix = torch.zeros((s * 3, s * 3))
        
        # Fill the new matrix with smaller copies of the original matrix
        for i in range(3):
            for j in range(3):
                if (i % 2 == 0 and j % 2 == 0) or (i == 1 and j == 1):
                    new_matrix[i*s:(i+1)*s, j*s:(j+1)*s] = matrix

        # Update the matrix for the next iteration
        matrix = new_matrix

    return matrix


plt.subplot(3,1,1)
for i in range(1,4):
  plt.subplot(3,1,i)

  # Set the number of iterations
  iterations = i

  # Generate the fractal
  fractal = vicsek_fractal(iterations)

  # Plot the fractal
  plt.imshow(fractal, cmap="Greys")
plt.axis('off')
plt.show()
