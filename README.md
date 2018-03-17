# pontopy
Aplicação CLI (Command Line Interface) em Python para registrar ponto no aplicativo PontoMais.

### Instalação

**Pontopy** pode ser insalado diretamente do repositório git, para instalar
execute o comando

```sh
 $ pip install git+https://github.com/Juroviol/pontopy.git
```

Dessa forma 

```sh
$ pontopy
```
estará disponível em linha do comando

### Modos de uso

1. Promt login e senha

    ```sh
    $ pontopy
    Login: <login>
    Senha: <senha>
    Ponto registrado com sucesso!
    ```

2. Credenciais como argumentos

    ```sh
    $ pontopy <login> <senha>
    Ponto registrado com sucesso!
    ```

3. Credenciais em cache

    ```sh
    $ pontopy
    Ponto registrado com sucesso!
    ```

    Essa forma é a mais rápida, porém só pode ser utilizada, se ao menos uma vez foi executado em uma das formas acima