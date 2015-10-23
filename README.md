# ProFunge
A production-ready fungeoidal programming language (eventually)
## Introduction
Hello, my name is hp, the designer and creater of the ProFunge programming language! I'd like to personally welcome you to my README.

Profunge is a fungeoidal programming language. What is a fungeoid? What makes it so new and special? Read on to find out.

## Fungeoids
A fungeoid is a (typically stack-oriented) programming language that does a lot of playing with instruction execution order. That's really all there is to it.

Specifically, a fungeoid plays with instruction execution by having the instruction pointer, or "IP", behave a bit differently from how it works in normal programming languages. In standard assembly language, assuming I understand it correctly, there is one IP. It moves, step by step, one at a time, through the program, only changing its order if the program tells it to jump. Even when it jumps, it still executes forwards, instruction-by-instruction.

In a fungeoid, this is different. A fungeoid allows the IP to move both forwards and backwards, and in the case of most funges, up and down. That's right. ProFunge is 2D.

Now, the original fungeoid, [http://esolangs.org/wiki/Befunge|Befunge], worked like this. However, it had one, glaring flaw: all instructions were single characters. This, needless to say, made it hard to read. Furthermore, Befunge-93 didn't support any form of libraries, or really anything more than what's necessary to simulate some push-down automata. Funge-98 remedies two of these issues, by allowing "Fingerprints", which were very limited sorts of libraries that had to be built-in to the interpreter, and an unbounded playfield which made it Turing-complete (at least, in the 2D and 3D versions, Befunge-98 and Trefunge-98. The 1D variant, Unefunge, is impossible to make TC while preserving the spirit of fungeoids). However, it was still hard to read, and its "Stack Stack" just made things confusing.

On to ProFunge!

## What makes ProFunge special?
ProFunge is a fungeoid much like Funge-98. It's stack-oriented, Turing-complete, and two-dimensional (well, it's similar to Befunge-98 in that respect, but not all of Funge-98). However, it has a few fairly major improvements:

1. ProFunge supports multi-character instructions by virtue of being encoded in CSV instead of just a plain text file (a special IDE is recommended so the code lines up properly)
2. ProFunge allows multiple instructions in a single cell if desired (though this is not always recommended, in the case that the programmer later wants to separate them and has to restructure their entire code to fit)
3. ProFunge allows multiple stacks, to avoid forcing the programmer to be constantly juggling the main stack-oriented
4. ProFunge supports OO, Dynamic Typing, and procedures (planned)
5. ProFunge allows libraries to be loaded easily, with libraries for Socketry, GUI, and advanced mathematics planned

## Why on Earth would I want to use this?
ProFunge is designed to be a new and interesting type of programming, made to take advantage of the Programmer's natural spatial reasoning. Though you are free to use it commercially (or within a company's infrastructure) and it is hoped it can support this, it was not explicitly designed for this purpose in its current form. Also, the current interpreter is made in Python and is slow. A C++-based interpreter for a better version is being speculated about. No compiler is planned. Like, ever.

### Are there any bugs?
Yes. ProFunge is being actively and concurrently designed and programmed, so it is chock-full of bugs. Feel free to report them! In fact, fell *obligated* to do so.

This version is not really made for serious usage, but it is a stepping stone to that.