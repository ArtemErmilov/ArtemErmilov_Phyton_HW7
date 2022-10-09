import User_interface as ui
import Loger as log
import breaking_data as bd
import Rational_math as rm
import Complex_math as cm
from os import system





def start_calc():
    log.log_data('Старт программы "Калькулятор"')
    new_start=True
    while True:
        if new_start==True:
            text_start="Необходимо выбрать с какими числами будете работать: \n1 - Работа с рациональными числами;\n2 - Работа с комплексными числами.\nВвод любого символа кроме 1 и 2 + Enter или Enter закончит программу калькулятора.\n=> "
            working_mode=ui.input_data(text_start)
        else:
            text_restart='Для продолжения работы нажмите Enter.\nДля выхода из Калькулятора введите любой символ и нажмите Enter.\n=> '
            working_mode=ui.input_data(text_restart)
            if working_mode=='':
                log.log_data('Пользователь выбрал продолжение работы программы "Калькулятор"')
                new_start=True
                system ('cls')
                continue
            else:
                text_end='Программа "Kалькулятор" закончила работу\n '
                log.log_data(text_end)
                ui.output_data(text_end)
                break

        if working_mode=='1': # Работа с рациональными числами
            log.log_data('Работа с рациональными числами')# Логирование начала работы

            text_rac='Введите математическое выражение с рациональными числами в виде -3+2*(2^3/7). \nДля математических операций используйте операторы  "-", "+","*", "/", "^"\n=> '
            rac_mac=ui.input_data(text_rac)# Введённое выражение
            log.log_data(f'Пользователь ввёл=> {rac_mac}')# Логирование
            
            
            bool_error,text_error, rac_number = rm.math_rational_namber(rac_mac)# решение

            if bool_error==False:
                ui.output_data(f'{rac_mac} = {rac_number}')
                log.log_data(f'Решение: {rac_mac} = {rac_number}')# Логирование ответ
            else:            
                ui.output_data(text_error)
                log.log_data('Ошибка. ' + text_error)# Логирование ошибки
            new_start=False

        elif working_mode=='2': # Работа с комплексными числами
            log.log_data('Работа с комплексными числами')

            text_komp='Введите выражения с комплексными числами в виде ((5+5i)+(2+3i))*(0+5i)\nДля математических операций используйте операторы  "-", "+","*", "/"\n=> '
            kompl_mac=ui.input_data(text_komp)
            log.log_data(f'Пользователь ввёл=> {kompl_mac}')

            bool_error,text_error, com_number = cm.math_compleks_namber(kompl_mac)

            if bool_error==False:
                ui.output_data(f'{kompl_mac} = {com_number}')
                log.log_data(f'Решение: {kompl_mac} = {com_number}')
            else:
                ui.output_data(text_error)
                log.log_data('Ошибка. ' + text_error)# Логирование ошибки
            new_start=False
        else:
            text_end='Программа "Kалькулятор" закончила работу\n '
            log.log_data(text_end)
            ui.output_data(text_end)
            break