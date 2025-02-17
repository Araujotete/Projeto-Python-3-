# Como enviar meu projeto Python para o GitHub

## Passo 1: Criar um repositório no GitHub
- Vá para [GitHub](https://github.com) e faça login.
- Clique no botão "New" para criar um novo repositório.
- Dê um nome ao seu repositório e clique em "Create repository".

## Passo 2: Inicializar um repositório Git localmente
### Windows
1. Pressione `Win + R` para abrir a janela "Executar".
2. Digite `cmd` e pressione `Enter` para abrir o Prompt de Comando.
3. Use o comando `cd` para navegar até o diretório do seu projeto. Por exemplo:
   ```sh
   cd "D:\ARQUIVOS E DOCUMENTOS\4 - ESTER ARAÚJO\Estudos (Cursos)\Python - Pythonando\Projetos\Aula 3 dnv"
   ```

### macOS
1. Pressione `Cmd + Space` para abrir o Spotlight.
2. Digite `Terminal` e pressione `Enter` para abrir o Terminal.
3. Use o comando `cd` para navegar até o diretório do seu projeto. Por exemplo:
   ```sh
   cd "/d:/ARQUIVOS E DOCUMENTOS/4 - ESTER ARAÚJO/Estudos (Cursos)/Python - Pythonando/Projetos/Aula 3 dnv"
   ```

### Linux
1. Abra o Terminal a partir do menu de aplicativos.
2. Use o comando `cd` para navegar até o diretório do seu projeto. Por exemplo:
   ```sh
   cd "/d:/ARQUIVOS E DOCUMENTOS/4 - ESTER ARAÚJO/Estudos (Cursos)/Python - Pythonando/Projetos/Aula 3 dnv"
   ```

## Passo 3: Adicionar os arquivos do seu projeto ao repositório local
```sh
git add .
```

## Passo 4: Fazer commit das suas mudanças
```sh
git commit -m "Initial commit"
```

## Passo 5: Conectar seu repositório local ao repositório remoto no GitHub
Substitua `<URL_DO_REPOSITORIO>` pela URL do repositório que você criou no GitHub.
```sh
git remote add origin <URL_DO_REPOSITORIO>
```

## Passo 6: Enviar (push) suas mudanças para o GitHub
```sh
git push -u origin master
```
