import codecs, sys

outf = codecs.getwriter('cp866')(sys.stdout, erors='replace')
sys.stdout = outf

age = raw_input(u"Сколько тебе лет?")
height = raw_input(u"Какой твой рост?")
weight = raw_input(u"Какой твой вес?")

print(u"Итак, тебе %лет, у тебя %рост, %кг вес" % (age, height, weight))
