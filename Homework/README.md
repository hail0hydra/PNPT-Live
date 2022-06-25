# Homeworks Assigned
<br>

- __This directory tracks ___HomeWorks___.__

<br>
<br>

>## Day 2 Homework

<br>
<br>


- :warning: Both of these scripts are made only for `TCP` ports.

- :warning: Additional support for `UDP` will be added soon! :sunglasses:. 

<br>
<br>

1. ___[(Discord)[Otty][22:28 - 2022,24 June]](https://discord.com/channels/542352179059752970/986065743303016518/989937639564140604)___
 ```
   Q. Write a network scanner in bash and a network scanner in python and run them. See which one finishes first.
```
<br>

- [x] created `pynmap.py` in `python` using `socket` __library/module__ in python

- [x] `bash` one created using `/dev/tcp`.

<br>
<br>
<br>

>### CONCLUSION:

Following we can see which script takes how much time.

```bash
    [ enum ~/Documents]$ time ./bashnmap.sh 10.0.2.4 4000
    --==[[ Bash Port Scanner by Hail_Hydra ]]==--
     
    22 on 10.0.2.4 open!
    1234 on 10.0.2.4 open!
    1337 on 10.0.2.4 open!
    2468 on 10.0.2.4 open!

    real	0m0.907s
    user	0m0.127s
    sys	0m0.059s
```
it takes around `0.907` seconds.

<br>

Let's see python one:

```bash
    [ enum ~/Documents]$ time ./pynmap  10.0.2.4 4000
    --==[[ Python Port Scanner by Hail_Hydra ]]==--


    Found Open Port : 22 
    Found Open Port : 1234 
    Found Open Port : 1337 
    Found Open Port : 2468 

    real	0m1.044s
    user	0m0.212s
    sys	0m0.089s
```

it takes around `1.044` seconds.

<br>
<br>

- Although this shows pretty clearly who wins, but that was not the case everytime. I had tried running these scripts several time and everytime, it was one or the other at the top.

<br>

- The result is still inconclusive and will be looked up on by a senior. :sunglasses:

<br>

---

<br>

- I asked the mods for help and [`Dewalt`](https://github.com/Dewalt-arch/pimpmykali) replied: 

    ```text
    Python is faster than Bash and is ranked 1st, while
    Bash is ranked 34th. The most important reasons 
    people chose Python are that it can be used for
    almost any task. It works on most 
    major operating systems and is also installed by default on most
    Unix/Linux systems.
    ```
    ---

- Hence we conclude that :metal: ___Python Rocks!!!___ :metal:


