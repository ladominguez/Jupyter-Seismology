! Este progrma te dice si eres mayor de edad

program mayor_edad
implicit none
integer :: edad
write (*,*) 'Este programa te dice si eres mayor de edad o no.'
do
    write (*,*) "Cuantos anios tienes?"  ! ñ, y signos de interrogacion y acentos omoitidos intencionalmente.
    read (*,*) edad
    if ( edad .lt. 18) then
        write (*,*) "Eres menor de edad. No tomar cerveza.\r"
    else
        write (*,*) "Eres mayor de edad. Saca tu credencial para votar.\r"
    endif 

end do
end program mayor_edad
