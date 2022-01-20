#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import random
import spade
import sys
import json
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message



class TicTacToe(Agent):
    class TicTacToeBehaviour(CyclicBehaviour):

        def printGrid(self, action):
            print(action)
            print()
            row = ""
            limiter = "-----------"
            counter = 0
            for el in self.ttt:
                if el[0] == 0:
                    row += "   "
                if el[0] == 1:
                    row += " O "
                if el[0] == 2:
                    row += " X "
                row += "|"
                if el[1] == 0:
                    row += "   "
                if el[1] == 1:
                    row += " O "
                if el[1] == 2:
                    row += " X "
                row += "|"
                if el[2] == 0:
                    row += "   "
                if el[2] == 1:
                    row += " O "
                if el[2] == 2:
                    row += " X "
                print (row)
                if counter <2:
                    print(limiter)
                row = ""
                counter +=1
            print()
            print()


        def checkGame(self):
            for el in self.ttt:
                if el[0] != 0 and (el[0] == el[1] == el[2]):
                    if el[0] == self.sign:
                        print("Pobjedio sam!")
                    else:
                        print("Izgubio sam!")
                    return True

            column = 0
            end = False
            for i in range(3):
                if self.ttt[0][i] != 0 and (self.ttt[0][i] == self.ttt[1][i] == self.ttt[2][i]):
                    end = True
                    column = i
                    break
            if end:
                if self.ttt[0][column] == self.sign:
                    print("Pobjedio sam!")
                else:
                    print("Izgubio sam!")
                return True

            if self.ttt[1][1] != 0 and ((self.ttt[0][0] == self.ttt[1][1] == self.ttt[2][2])
              or(self.ttt[0][2] == self.ttt[1][1] == self.ttt[2][0])):
                if self.ttt[1][1] == self.sign:
                    print("Pobjedio sam!")
                else:
                    print("Izgubio sam!")
                return True

            all_full = True
            for el in self.ttt:
                for e in el:
                    if e == 0:
                        all_full = False

            if all_full:
                print("Izjednaceno!")
                return True
            else:
                return False


        def checkOneToWin(self, sign):
            counter = 0
            for el in self.ttt:
                if el[0] == sign and el[0] == el[1] and el[2] == 0:
                    return [True, counter, 2]
                if el[0] == sign and el[0] == el[2] and el[1] == 0:
                    return [True, counter, 1]
                if el[1] == sign and el[1] == el[2] and el[0] == 0:
                    return [True, counter, 0]
                counter += 1

            for i in range(3):
                if self.ttt[0][i] == sign and self.ttt[0][i] == self.ttt[1][i] and self.ttt[2][i] == 0:
                    return [True, 2, i]
                if self.ttt[0][i] == sign and self.ttt[0][i] == self.ttt[2][i] and self.ttt[1][i] == 0:
                    return [True, 1, i]
                if self.ttt[1][i] == sign and self.ttt[1][i] == self.ttt[2][i] and self.ttt[0][i] == 0:
                    return [True, 0, i]

            if self.ttt[0][0] == sign and self.ttt[0][0] == self.ttt[1][1] and self.ttt[2][2] == 0:
                return [True, 2, 2]
            if self.ttt[0][0] == sign and self.ttt[0][0] == self.ttt[2][2] and self.ttt[1][1] == 0:
                return [True, 1, 1]
            if self.ttt[1][1] == sign and self.ttt[1][1] == self.ttt[2][2] and self.ttt[0][0] == 0:
                return [True, 0, 0]

            if self.ttt[0][2] == sign and self.ttt[0][2] == self.ttt[1][1] and self.ttt[2][2] == 0:
                return [True, 2, 2]
            if self.ttt[0][2] == sign and self.ttt[0][2] == self.ttt[2][0] and self.ttt[1][1] == 0:
                return [True, 1, 1]
            if self.ttt[1][1] == sign and self.ttt[1][1] == self.ttt[2][0] and self.ttt[0][2] == 0:
                return [True, 0, 2]
            return[False, 0, 0]


        def playFirstEmpty(self):
            found = False
            for e in self.ttt:
                y = 0
                for el in e:
                    if el == 0:
                        e[y] = self.sign
                        found = True
                        break
                    y += 1
                if found:
                    break
            return found


        def putAtIndex(self, x, y):
            counter = 0
            for el in self.ttt:
                if counter == x:
                    el[y]=self.sign
                    break
                counter += 1


        def playRandom(self):
            found = False
            while not found:
                x = random.randint(0, 2)
                y = random.randint(0, 2)
                if self.ttt[x][y]==0:
                    found = True
                    self.putAtIndex(x,y)
            return found

        def playRandomWithWinCheck(self):
            result = self.checkOneToWin(self.sign)
            if result[0]:
                self.putAtIndex(result[1],result[2])
                return True
            result = self.checkOneToWin(self.opponentSign)
            if result[0]:
                self.putAtIndex(result[1], result[2])
                return True
            found = False
            while not found:
                x = random.randint(0, 2)
                y = random.randint(0, 2)
                if self.ttt[x][y] == 0:
                    found = True
                    self.putAtIndex(x, y)
            return found

        def playMiddleWithWinCheck(self):
            result = self.checkOneToWin(self.sign)
            if result[0]:
                self.putAtIndex(result[1],result[2])
                return True
            result = self.checkOneToWin(self.opponentSign)
            if result[0]:
                self.putAtIndex(result[1], result[2])
                return True
            if self.ttt[1][1] == 0:
                self.putAtIndex(1,1)
                return True
            found = False
            while not found:
                x = random.randint(0, 2)
                y = random.randint(0, 2)
                if self.ttt[x][y] == 0:
                    found = True
                    self.putAtIndex(x, y)
            return found


        def checkCornerPlay(self, sign):
            if self.ttt[0][0] == sign and self.ttt[2][2] == sign and \
                    self.ttt[0][1] == 0 and self.ttt[0][2] == 0 and self.ttt[1][2] == 0:
                return [True, 0, 2]
            if self.ttt[0][0] == sign and self.ttt[2][2] == sign and \
                    self.ttt[1][0] == 0 and self.ttt[2][0] == 0 and self.ttt[2][1] == 0:
                return [True, 2, 0]
            if self.ttt[0][2] == sign and self.ttt[2][0] == sign and \
                    self.ttt[0][0] == 0 and self.ttt[0][1] == 0 and self.ttt[1][0] == 0:
                return [True, 0, 0]
            if self.ttt[0][2] == sign and self.ttt[2][0] == sign and \
                    self.ttt[1][2] == 0 and self.ttt[2][2] == 0 and self.ttt[2][1] == 0:
                return [True, 2, 2]

            if self.ttt[0][0] == sign and self.ttt[2][2] == 0 and \
                    self.ttt[0][1] == 0 and self.ttt[0][2] == 0 and self.ttt[1][2] == 0:
                return [True, 2, 2]
            if self.ttt[0][0] == 0 and self.ttt[2][2] == sign and \
                    self.ttt[0][1] == 0 and self.ttt[0][2] == 0 and self.ttt[1][2] == 0:
                return [True, 0, 0]
            if self.ttt[0][0] == sign and self.ttt[2][2] == 0 and \
                    self.ttt[1][0] == 0 and self.ttt[2][0] == 0 and self.ttt[2][1] == 0:
                return [True, 2, 2]
            if self.ttt[0][0] == 0 and self.ttt[2][2] == sign and \
                    self.ttt[1][0] == 0 and self.ttt[2][0] == 0 and self.ttt[2][1] == 0:
                return [True, 0, 0]

            if self.ttt[0][2] == sign and self.ttt[2][0] == 0 and \
                    self.ttt[0][0] == 0 and self.ttt[0][1] == 0 and self.ttt[1][0] == 0:
                return [True, 2, 0]
            if self.ttt[0][2] == 0 and self.ttt[2][0] == sign and \
                    self.ttt[0][0] == 0 and self.ttt[0][1] == 0 and self.ttt[1][0] == 0:
                return [True, 0, 2]
            if self.ttt[0][2] == sign and self.ttt[2][0] == 0 and \
                    self.ttt[1][2] == 0 and self.ttt[2][2] == 0 and self.ttt[2][1] == 0:
                return [True, 2, 0]
            if self.ttt[0][2] == 0 and self.ttt[2][0] == sign and \
                    self.ttt[1][2] == 0 and self.ttt[2][2] == 0 and self.ttt[2][1] == 0:
                return [True, 0, 2]

            if self.ttt[0][0] == 0 and self.ttt[2][2] == 0 and \
                    self.ttt[0][1] == 0 and self.ttt[0][2] == 0 and self.ttt[1][2] == 0:
                return [True, 0, 0]
            if self.ttt[0][0] == 0 and self.ttt[2][2] == 0 and \
                    self.ttt[1][0] == 0 and self.ttt[2][0] == 0 and self.ttt[2][1] == 0:
                return [True, 0, 0]
            if self.ttt[0][2] == 0 and self.ttt[2][0] == 0 and \
                    self.ttt[0][0] == 0 and self.ttt[0][1] == 0 and self.ttt[1][0] == 0:
                return [True, 0, 2]
            if self.ttt[0][2] == 0 and self.ttt[2][0] == 0 and \
                    self.ttt[1][2] == 0 and self.ttt[2][2] == 0 and self.ttt[2][1] == 0:
                return [True, 0, 2]
            return [False, 0, 0]



        def checkThroughMiddle(self, sign):
            if self.ttt[0][0] == sign and self.ttt[2][0] == sign and \
                    self.ttt[0][1] == 0 and self.ttt[0][2] == 0 and self.ttt[1][1] == 0:
                return [True, 0, 2]
            if self.ttt[0][0] == sign and self.ttt[2][0] == sign and \
                    self.ttt[2][1] == 0 and self.ttt[2][2] == 0 and self.ttt[1][1] == 0:
                return [True, 2, 2]
            if self.ttt[0][0] == sign and self.ttt[0][2] == sign and \
                    self.ttt[2][0] == 0 and self.ttt[1][0] == 0 and self.ttt[1][1] == 0:
                return [True, 2, 0]
            if self.ttt[0][0] == sign and self.ttt[0][2] == sign and \
                    self.ttt[1][2] == 0 and self.ttt[2][2] == 0 and self.ttt[1][1] == 0:
                return [True, 2, 2]
            if self.ttt[0][2] == sign and self.ttt[2][2] == sign and \
                    self.ttt[0][0] == 0 and self.ttt[0][1] == 0 and self.ttt[1][1] == 0:
                return [True, 0, 0]
            if self.ttt[0][2] == sign and self.ttt[2][2] == sign and \
                    self.ttt[2][0] == 0 and self.ttt[2][1] == 0 and self.ttt[1][1] == 0:
                return [True, 2, 0]
            if self.ttt[2][0] == sign and self.ttt[2][2] == sign and \
                    self.ttt[1][0] == 0 and self.ttt[0][0] == 0 and self.ttt[1][1] == 0:
                return [True, 0, 0]
            if self.ttt[2][0] == sign and self.ttt[2][2] == sign and \
                    self.ttt[1][2] == 0 and self.ttt[0][2] == 0 and self.ttt[1][1] == 0:
                return [True, 0, 2]
            return [False, 0, 0]

        def playCornerWithWinCheck(self):
            result = self.checkOneToWin(self.sign)
            if result[0]:
                self.putAtIndex(result[1],result[2])
                return True
            result = self.checkOneToWin(self.opponentSign)
            if result[0]:
                self.putAtIndex(result[1], result[2])
                return True
            result = self.checkCornerPlay(self.sign)
            if result[0]:
                self.putAtIndex(result[1], result[2])
                return True
            result = self.checkThroughMiddle(self.sign)
            if result[0]:
                self.putAtIndex(result[1], result[2])
                return True
            if self.ttt[1][1] == 0:
                self.putAtIndex(1,1)
                return True
            found = False
            while not found:
                x = random.randint(0, 2)
                y = random.randint(0, 2)
                if self.ttt[x][y] == 0:
                    found = True
                    self.putAtIndex(x, y)
            return found

        def playTurn(self):
            found = False
            if self.checkGame():
                return [found, True]

            if self.intelligence == 1:
                found = self.playFirstEmpty()
            elif self.intelligence == 2:
                found = self.playRandom()
            elif self.intelligence == 3:
                found = self.playRandomWithWinCheck()
            elif self.intelligence == 4:
                found = self.playMiddleWithWinCheck()
            elif self.intelligence == 5:
                found = self.playCornerWithWinCheck()
            else:
                found = self.playFirstEmpty()

            time.sleep(2)
            self.printGrid("Odigrao:")

            return [found, self.checkGame()]


        async def run(self):
            if self.turn == 2:
                msg = await self.receive(timeout=10)
                if msg:
                    self.ttt = json.loads(msg.body)
                    self.printGrid("Primio:")
                    result = self.playTurn()
                    if result[0]:
                        msg = spade.message.Message(
                            to=self.opponent,
                            body=json.dumps(self.ttt),
                            metadata={
                                "ontology": "TicTacToe",
                                "language": "english",
                                "performative": "inform"})
                        await self.send(msg)
                    if result[1]:
                        while True:
                            time.sleep(100)
                else:
                    print("Cekam drugog igraca!")
            elif self.turn == 1:
                self.playTurn()
                msg = spade.message.Message(
                    to=self.opponent,
                    body=json.dumps(self.ttt),
                    metadata={
                        "ontology": "TicTacToe",
                        "language": "english",
                        "performative": "inform"})
                await self.send(msg)
                self.turn = 2
            else:
                print("Krivo postavljen potez!")
                time.sleep(10)


        async def on_start(self):
            self.ttt = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            self.sign = int(str(Message(to=self.get("turn")).to))
            self.turn = int(str(Message(to=self.get("turn")).to))
            self.intelligence = int(str(Message(to=self.get("intelligence")).to))
            self.opponent = str(Message(to=self.get("opponent")).to)
            if self.sign == 1:
                self.opponentSign = 2
                print("Igram: O")
                print()
            elif self.sign == 2:
                self.opponentSign = 1
                print("Igram: X")
                print()



    async def setup(self):
        print("TicTacToe player: Starting!")

        TicTacToeTemplate = spade.template.Template(
            metadata={"ontology": "TicTacToe"}
        )
        behaviourSP = self.TicTacToeBehaviour()
        self.add_behaviour(behaviourSP, TicTacToeTemplate)

if __name__ == '__main__':
    args = sys.argv
    if len(args) == 6:
        player = TicTacToe(args[1], args[2])
        player.set("turn", args[3])
        player.set("intelligence", args[4])
        player.set("opponent", args[5])
        player.start()


        input("Press ENTER to exit.\n")
        player.stop()
        spade.quit_spade()
    else:
        print("Krivi broj argumenata")