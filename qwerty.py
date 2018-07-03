import sympy
import logging

logging.basicConfig(format = u'time:"%(asctime)s",levelname:"%(levelname)-1s",message:"%(message)s"', level = logging.DEBUG, filename = u'logfile.log')

nameFile=input();

try:
    with open(nameFile, "r") as t:
        for line in t:
            logging.info("equation: %s, result: %s" % (line, sympy.solve(line)))
            print(sympy.solve(line))


except:
    print('Какая-то ошибка')
    logging.error('Error')

