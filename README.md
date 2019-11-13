<h1 align="center">
<p>PIKALANG - The Pikachu Programming Language</p>
<br>
<img style="margin-bottom:-14px" src="images/shock.gif" />
<br>
</h1>

A [brainfuck][2] derivative based off the vocabulary of [Pikachu][3] from [Pokémon][4].

Syntax
------
pikalang  | brainfuck | description                                   
----------|-----------|-----------------------------------------------
`pi`      | +         | increment the byte at pointer                 
`ka`      | -         | decrement the byte at pointer                 
`pika`    | [         | if pointer is zero, jump to matching `chu`    
`chu`     | ]         | if pointer is nonzero, jump to matching `pika`
`pipi`    | >         | increment the data pointer                    
`pichu`   | <         | decrement the data pointer                    
`pikapi`  | ,         | input of one byte into pointer                
`pikachu` | .         | output the byte at pointer                    


Installation
------------
stable:
```shell
pip install pikalang
```

or bleeding edge...
```shell
git clone https://github.com/grotewold/pikalang.git
cd pikalang

python setup.py install
```


Usage
-----
```shell
pikalang path/to/file.pokeball
```


File Extention
--------------
A pikalang program must be stored in a file with a `.pokeball` extention


API Usage
---------
```python
import pikalang

sourcecode = """
    pi pi pi pi pi pi pi pi pi pi pika pipi pi pi pi pi pi pi pi pipi pi pi pi
    pi pi pi pi pi pi pi pipi pi pi pi pipi pi pichu pichu pichu pichu ka chu
    pipi pi pi pikachu pipi pi pikachu pi pi pi pi pi pi pi pikachu pikachu pi
    pi pi pikachu pipi pi pi pikachu pichu pichu pi pi pi pi pi pi pi pi pi pi
    pi pi pi pi pi pikachu pipi pikachu pi pi pi pikachu ka ka ka ka ka ka
    pikachu ka ka ka ka ka ka ka ka pikachu pipi pi pikachu pipi pikachu
    """

# or use sourcecode = pikalang.load_source("FILENAME.pokeball") to load from file

pikalang.evaluate(sourcecode)
```

Development
-----------
When developing, use `pipenv` to install needed tools.

```sh
pipenv install

pipenv run black .

pipenv run python -m pikalang tests/hello-world.pokeball
```

Thanks
------
Special thanks to [Elliot Chance][5] for providing the base implementation of this.

Disclaimer
----------
This is a fan-based parody of themes from [Pokémon][3]. The language,
as well as its author, is in no way associated with the Pokémon francise
and its creators, nor is this project, in any way, for-profit. This is a
project to teach myself `ply`, which is protected under fair use.


[1]: http://esolangs.org/wiki/Pikalang
[2]: http://en.wikipedia.org/wiki/Brainfuck "Brainfuck"
[3]: https://www.google.com/search?q=pikachu&tbm=isch "Pikachu"
[4]: http://www.pokemon.com/ "Pokémon"
[5]: http://elliot.land/post/write-your-own-brainfuck-interpreter "Elliot Chance"
