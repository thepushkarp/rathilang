<p align="center"><a href="https://aashutosh.dev/"><img style="margin-bottom:-14px" src="https://user-images.githubusercontent.com/42088801/68935859-4c642180-07bf-11ea-9c2b-98559ff94f32.png" width="175"></a></p>
<h1 align="center">RATHILANG - The Allstack Programming Language</h1>
<p align="center">
<p align="center">
<a href="https://pypi.org/project/rathilang/"><img alt="PyPI" src="https://img.shields.io/pypi/v/rathilang?style=for-the-badge"></a>
<a href="https://travis-ci.com/thepushkarp/rathilang"><img alt="Travis (.com)" src="https://img.shields.io/travis/com/thepushkarp/rathilang?style=for-the-badge"></a>
<a href="https://github.com/thepushkarp/rathilang/issues"><img src="https://img.shields.io/github/issues/thepushkarp/rathilang?style=for-the-badge"></a>
</p>
<hr>
<p align="center"><a href="http://en.wikipedia.org/wiki/Brainfuck">A brainfuck</a> derivative based on the the characteristics of <a href="https://aashutosh.dev/">Aashutosh Rathi</a></p>


Syntax
------
rathilang    | brainfuck | description                                   
-------------|-----------|-----------------------------------------------
`jiren`      | +         | increment the byte at pointer                 
`bakar`      | -         | decrement the byte at pointer                 
`allstack`   | [         | if pointer is zero, jump to matching `developer`    
`developer`  | ]         | if pointer is nonzero, jump to matching `allstack`
`rathi`      | >         | increment the data pointer                    
`aashutosh`  | <         | decrement the data pointer                    
`abeteri`    | ,         | input of one byte into pointer                
`pitega`     | .         | output the byte at pointer


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
rathilang path/to/file.baka
```


File Extention
--------------
A rathilang program must be stored in a file with a `.baka` extention because `rathilang` doesn't considers any other file worthy enough.


API Usage
---------
```python
import rathilang

sourcecode = """
    jiren jiren jiren jiren jiren jiren jiren jiren jiren jiren allstack rathi jiren rathi jiren jiren jiren 
    rathi jiren jiren jiren jiren jiren jiren jiren rathi jiren jiren jiren jiren jiren jiren jiren jiren jiren 
    jiren aashutosh aashutosh aashutosh aashutosh bakar developer rathi rathi rathi jiren jiren pitega rathi 
    jiren pitega jiren jiren jiren jiren jiren jiren jiren pitega pitega jiren jiren jiren pitega aashutosh 
    aashutosh jiren jiren pitega rathi bakar bakar bakar bakar pitega rathi bakar bakar bakar bakar bakar bakar 
    bakar bakar bakar bakar pitega jiren jiren jiren jiren jiren jiren jiren jiren jiren jiren jiren jiren jiren 
    jiren jiren jiren jiren pitega bakar bakar bakar pitega aashutosh aashutosh jiren pitega aashutosh jiren 
    jiren jiren jiren jiren jiren jiren jiren jiren jiren pitega"""

# or use sourcecode = rathilang.load_source("FILENAME.allstack") to load from file

rathilang.evaluate(sourcecode)
```

Development
-----------
When developing, use `pipenv` to install needed tools.

```sh
pipenv install

pipenv run black .

pipenv run python -m rathilang tests/hello-devs.baka
```

Thanks
------
Special thanks to [Elliot Chance][4] for providing the base implementation of this and [Pikalang][1] for providing the implementation on top of which this repo is made.

Disclaimer
----------
This is a small gift for [Aashutosh Rathi][3] who did big things for the institute and me. The [pikalang][1] repository served as an inspiration for me. This repository is protected under fair use.

[1]: https://github.com/groteworld/pikalang "Pikalang"
[2]: http://en.wikipedia.org/wiki/Brainfuck "Brainfuck"
[3]: https://aashutosh.dev/ "Aashutosh Rathi"
[4]: http://elliot.land/post/write-your-own-brainfuck-interpreter "Elliot Chance"

<p align="center"> Made with ❤️ by <a href="https://github.com/thepushkarp">Pushkar Patel</a> </p>