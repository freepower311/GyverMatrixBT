import os

modes = [ 'fillString("С НОВЫМ ГОДОМ !", 1);', \
          'cloudNoise();', \
          'fillString("2022", 2);', \
          'lavaNoise();', \
          'fillString("С НОВЫМ ГОДОМ !", 3);', \
          'plasmaNoise();', \
          'fillString("2022", 1);', \
          'rainbowNoise();', \
          'fillString("С НОВЫМ ГОДОМ !", 4);', \
          'rainbowStripeNoise();', \
          'fillString("2022", 1);', \
          'zebraNoise();', \
          'fillString("С НОВЫМ ГОДОМ !", 255);', \
          'forestNoise();', \
          'fillString("2022", 1);', \
          'oceanNoise();', \
          'fillString("С НОВЫМ ГОДОМ !", 255255);', \
          'snowRoutine();', \
          'fillString("2022", 1);', \
          'sparklesRoutine();', \
          'fillString("С НОВЫМ ГОДОМ !", 65000);', \
          'matrixRoutine();', \
          'fillString("2022", 1);', \
          'starfallRoutine();', \
          'fillString("С НОВЫМ ГОДОМ !", 10000);', \
          'ballsRoutine();', \
          'fillString("2022", 100000);', \
          'rainbowRoutine();', \
          'fillString("С НОВЫМ ГОДОМ !", 200000);', \
          'fireRoutine();', \
          'fillString("2022", 150000);', \
          'snakeRoutine();', \
          'fillString("С НОВЫМ ГОДОМ !", 700);', \
          'tetrisRoutine();', \
          'fillString("2022", 15000);' ]

outfile = open('switch.txt', 'w')
outfile.write('  switch (thisMode) {\n')

count = 0
for mode in modes:
	outfile.write('    case ' + str(count) + ': ' + mode + '\n')
	outfile.write('      break;\n')
	count += 1

outfile.write('  }\n')
