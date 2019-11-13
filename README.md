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
`jiren`      | +         | increment the byte at pointer                 
`bakar`      | -         | decrement the byte at pointer                 
`fullstack`    | [         | if pointer is zero, jump to matching `developer`    
`developer`     | ]         | if pointer is nonzero, jump to matching `fullstack`
`rathi`    | >         | increment the data pointer                    
`aashutosh`   | <         | decrement the data pointer                    
`abeteri`  | ,         | input of one byte into pointer                
`pitega` | .         | output the byte at pointer                    


Installation
------------
stable:
```shell
pip install rathilang
```

or bleeding edge...
```shell
git clone https://github.com/thepushkarp/rathilang.git
cd rathilang

python setup.py install
```


Usage
-----
```shell
rathilang path/to/file.allstack
```


File Extention
--------------
A rathilang program must be stored in a file with a `.allstack` extention


API Usage
---------
```python
import rathilang

sourcecode = """
    bakar fullstack bakar bakar bakar bakar bakar
    bakar bakar rathi jiren aashutosh developer 
    rathi bakar pitega bakar fullstack bakar rathi 
    jiren jiren jiren jiren jiren aashutosh 
    developer rathi jiren jiren pitega jiren jiren 
    jiren jiren jiren jiren jiren pitega pitega 
    jiren jiren jiren pitega fullstack bakar bakar 
    bakar rathi jiren aashutosh developer rathi 
    bakar bakar bakar bakar bakar pitega jiren 
    jiren fullstack bakar rathi jiren jiren 
    aashutosh developer rathi pitega fullstack 
    bakar bakar rathi jiren jiren jiren aashutosh 
    developer rathi bakar pitega fullstack bakar 
    bakar bakar rathi jiren aashutosh developer 
    rathi bakar pitega bakar bakar bakar pitega
    """

# or use sourcecode = rathilang.load_source("FILENAME.allstack") to load from file

rathilang.evaluate(sourcecode)
```

Development
-----------
When developing, use `pipenv` to install needed tools.

```sh
pipenv install

pipenv run black .

pipenv run python -m rathilang tests/hello-world.allstack
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
