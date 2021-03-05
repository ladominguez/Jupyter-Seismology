
subroutine func_area(radio, area)
    real :: radio, area, pi
    pi   = 4.0*atan(1.0)
    area = pi*radio**2
    return
end
