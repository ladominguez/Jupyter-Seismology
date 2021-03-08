

program arreglos
   implicit none
   real :: numeros(10)           ! Arreglo de una sola dimension
   real :: matriz(3,3)
   integer :: i , j ! Arreglo de 2 dimensiones 

   ! Se le asigna la tabla de 4
   print *, "Tabla del 4"
   do i=1,10
      numeros(i) = i * 4.0
   end do

   ! Muestra los valores
   do i = 1, 10
      Print *, i, "x4=", numeros(i)
   end do

   ! Asigna valores a la matriz
   do i=1,3
      do j = 1, 3
         matriz(i, j) = i+j
      end do
   end do

   ! Muestra valores
   Print *, "//Imprime matriz"
   do i=1,3
      do j = 1, 3
         write(*, fmt="(A, i4, A, i4, A, f5.2, A)", advance="no") "i: ", i, " j: ", j, " = ", matriz(i,j), ", "
         ! Print *, i, "-" , j, "-",  matriz(i,j)   Mas facil de usar
      end do
         write(*,*) ""   ! Nuevas líneas
   end do

   ! Asigna valores directamente
   print  *, "Asignacion directa de valores."
   numeros = (/1.5, 3.2,4.5,0.9,7.2, 3.6, 8.9, 3.1, 9.2, 0.2 /)

   ! Muestra valores
   do i = 1, 10
      Print *, i, '-', numeros(i)
   end do

end program arreglos
