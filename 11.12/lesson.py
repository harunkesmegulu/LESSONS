{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<center><img src=\"https://github.com/aaron-clarusway/fullstack/blob/master/itf-logo.png?raw=true\"  alt=\"alt text\" width=\"200\"/></center>\n",
    "<br>\n",
    "<h1><p style=\"text-align: center; color:darkblue\">Python Basic</p><h1>\n",
    "<center><h1>Workshop - 2</h1></center>\n",
    "<p><img align=\"right\"\n",
    "  src=\"https://secure.meetupstatic.com/photos/event/3/1/b/9/600_488352729.jpeg\"  width=\"15px\"></p>\n",
    "<br>\n",
    "\n",
    "\n",
    "# Subject: Collections - Control Flow Statements"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Coding Challenge-1 : Find the Largest Number\n",
    "\n",
    "Purpose of the this coding challenge is to solve a simple sorting problem in Python.\n",
    "\n",
    "### Learning Outcomes\n",
    "\n",
    "At the end of the this coding challenge, students will be able to;\n",
    "\n",
    "- get a basic understanding of sorting algorithms.\n",
    "- demonstrate their knowledge of lists in python\n",
    "- implement loops to solve the problems in python\n",
    "- get a better understanding of computational thinking concepts\n",
    "\n",
    "### Problem Statement\n",
    "  \n",
    "- Write a python code that finds the largest number among the ``n`` numbers given by the user as input.\n",
    "\n",
    "- First, take `n` from the user, then take `n` numbers one by one and select-print the largest one.\n",
    "\n",
    "- It is forbidden to use ``max()`` function.  \n",
    "\n",
    "- Indicate which computational thinking concepts have you used.\n",
    "\n",
    "- Example for user inputs and respective outputs\n",
    "\n",
    "```text\n",
    "Input                Output\n",
    "---------------:     -------------------------:\n",
    "n = 5, 1 2 3 4 5     The largest number is:  5\n",
    "n = 3, 67 85 19      The largest number is:  85\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Solution :"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "How many numbers will you enter?7\n",
      "Please enter the number: 6\n",
      "Please enter the number: 6\n",
      "Please enter the number: 6\n",
      "Please enter the number: 6\n",
      "Please enter the number: 6\n",
      "Please enter the number: 6\n",
      "Please enter the number: 65\n",
      "The largest number is :  65\n"
     ]
    }
   ],
   "source": [
    "count=0\n",
    "array=[]\n",
    "size = int(input(\"How many numbers will you enter? \"))\n",
    "while count < size:\n",
    "    number= int(input('Please enter the number: '))\n",
    "    array.append(number)\n",
    "    count = count +1\n",
    "\n",
    "largest = array[0]\n",
    "for i in array:\n",
    "    if i > largest:\n",
    "        largest = i\n",
    "\n",
    "print(\"The largest number is : \", largest)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Coding Challenge-2 : Group Anagrams\n",
    "\n",
    "Purpose of the this coding challenge is to solve a grouping algorithm in Python.\n",
    "\n",
    "### Learning Outcomes\n",
    "\n",
    "At the end of the this coding challenge, students will be able to;\n",
    "\n",
    "- get a basic understanding of grouping algorithms.\n",
    "- demonstrate their knowledge of lists, dicts in python\n",
    "- implement loops to solve the problems in python\n",
    "- get a better understanding of computational thinking concepts\n",
    "\n",
    "### Problem Statement\n",
    "  \n",
    "- Given a list of strings, group anagrams together.\n",
    "\n",
    "- Example:\n",
    "\n",
    "**Input:**\n",
    "```\n",
    "[\"eat\", \"tea\", \"tan\", \"ate\", \"nat\", \"bat\"],\n",
    "Output:\n",
    "[\n",
    "  [\"ate\",\"eat\",\"tea\"],\n",
    "  [\"nat\",\"tan\"],\n",
    "  [\"bat\"]\n",
    "]\n",
    "```\n",
    "Note:\n",
    "All inputs will be in lowercase.\n",
    "The order of your output does not matter."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Solution :"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat'], ['cat', 'tac']]\n"
     ]
    }
   ],
   "source": [
    "strs = [\"eat\", \"tea\", \"tan\", \"ate\", \"nat\", \"bat\", \"cat\", \"tac\"]\n",
    "anag = {}\n",
    "for i in strs:\n",
    "    element = \"\".join(sorted(i))\n",
    "    if element in anag:\n",
    "        anag[element].append(i)\n",
    "    else:\n",
    "        anag[element] = [i]\n",
    "print(list(anag.values()))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}