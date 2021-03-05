program area_main 
implicit none
real :: r, area
write (*,*) "Este programa calcula el area de un circulo."
do
    write (*,*) "radio:"
    read  (*,*) r
    call func_area(r, area)
    write (*,*) "Area:"
    write (*,*) area
end do

end program area_main
