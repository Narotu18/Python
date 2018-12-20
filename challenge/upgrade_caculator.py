# Autor: Naruto_da
# -*- coding:utf-8 -*-
#!/usr/bin/env python
import sys
def real_compute(salary,tax,deduct):
    salary_id=salary.split(':')[0]
    salary_mon=int(salary.split(':')[1])
    social = salary_mon*0.08 + salary_mon*0.02 + salary_mon*0.005 +salary_mon*0.06    #五险一金
    pay_tax = (salary_mon-3500-social)*tax-deduct    #纳税额
    print(pay_tax)
    last_payment = salary_mon-social-pay_tax
    print("{}:{:.2f}".format(salary_id,last_payment))
def real_salary():
    for salary_person in sys.argv[1:]:
        try:
            if salary_person.split(':')[0].isdigit() and salary_person.split(':')[1].isdigit():
                salary = int(salary_person.split(':')[1])
                payment = salary-3500
                if 0<payment <= 1500:
                    real_compute(salary_person,0.03,0)
                elif payment >1500 and payment <=4500:
                    real_compute(salary_person,0.1,105)
                elif payment >4500 and payment <=9000:
                    real_compute(salary_person,0.2,555)
                elif payment >9000 and payment <=35000:
                    real_compute(salary_person,0.25,1005)
                elif payment > 35000 and payment <= 55000:
                    real_compute(salary_person,0.3,2755)
                elif payment > 55000 and payment <= 80000:
                    real_compute(salary_person,0.35,5505)
                elif payment >80000:
                    real_compute(salary_person,0.45,13505)
                else:
                    real_compute(salary_person,0,0)
            else:
                raise ValueError("Parameter Error: {0}".format(salary))
        except ValueError as err:
            print(err)

if __name__ == '__main__':
    real_salary()
