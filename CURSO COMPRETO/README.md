# INSTRUÇÕES (GENERICAS - PYSIDE6)
## 01-02) INTRODUÇÃO E PRIMEIRA JANELA 
**PySide** é um conjunto de bindings (ligações) para a biblioteca GUI Qt desenvolvida pela The Qt Company. Ele permite que você crie interfaces gráficas de usuário (GUIs) para aplicações usando a linguagem de programação Python. A biblioteca Qt é amplamente utilizada no desenvolvimento de software por sua flexibilidade, facilidade de uso e poderosas capacidades de design de interface.

### Conceitos Principais
1. **Qt Framework**:
   - O Qt é um framework multiplataforma para o desenvolvimento de interfaces gráficas de usuário (GUIs) e aplicações que podem ser executadas em várias plataformas, como Windows, macOS, Linux, iOS e Android.
   - Qt fornece uma ampla gama de funcionalidades, incluindo widgets para criação de interfaces, gráficos, acesso a bases de dados, redes, entre outros.

2. **Binding**:
   - Bindings são conexões que permitem que uma linguagem de programação use funcionalidades de bibliotecas escritas em outra linguagem. No caso do PySide, ele fornece bindings para que possamos usar o Qt com Python.

3. **Widgets**:
   - Widgets são componentes básicos da GUI, como botões, caixas de texto, rótulos, etc. Eles são os blocos de construção fundamentais de qualquer interface gráfica.

### Instalando PySide
Antes de começarmos a programar com PySide, é necessário instalá-lo. Você pode fazer isso usando o `pip`:

```sh
pip install PySide6
```

### Exemplo de Código: "Hello, World!" com PySide
Aqui está um exemplo simples de uma aplicação "Hello, World!" usando PySide:

```python
import sys
from PySide6.QtWidgets import QApplication, QLabel

# Cria uma aplicação Qt
app = QApplication(sys.argv)

# Cria um rótulo (label) com o texto "Hello, World!"
label = QLabel("Hello, World!")

# Mostra o rótulo na tela
label.show()

# Executa o loop da aplicação
sys.exit(app.exec())
```

### Explicação do Código
1. **Importações**:
   - `import sys`: Importa o módulo sys, necessário para manipular argumentos e sair do programa.
   - `from PySide6.QtWidgets import QApplication, QLabel`: Importa as classes QApplication e QLabel do módulo QtWidgets do PySide6.

2. **Criação da Aplicação Qt**:
   - `app = QApplication(sys.argv)`: Cria uma instância da aplicação Qt. `sys.argv` é passado para permitir o uso de argumentos de linha de comando.

3. **Criação do Widget**:
   - `label = QLabel("Hello, World!")`: Cria um rótulo com o texto "Hello, World!".

4. **Mostra o Widget**:
   - `label.show()`: Exibe o rótulo na tela.

5. **Executa o Loop da Aplicação**:
   - `sys.exit(app.exec())`: Inicia o loop da aplicação Qt e garante que o script Python seja encerrado corretamente quando a aplicação for fechada.

### Conclusão
Este exemplo básico demonstra como criar uma aplicação Qt com PySide. Conforme você avançar, poderá explorar widgets mais complexos, layouts, eventos e sinais, integração com bases de dados, gráficos e muito mais. PySide é uma ferramenta poderosa para criar interfaces de usuário ricas e interativas em Python.

## 03) CONFIGURANDO TAMANHOS DA JANELA
Para criar interfaces de usuário eficazes e responsivas, é essencial saber como configurar e ajustar os tamanhos das janelas e dos widgets. Em PySide, isso é feito principalmente usando métodos disponíveis nas classes de widgets e janelas.

### Conceitos Principais
1. **Tamanho Mínimo e Máximo**:
   - Você pode definir o tamanho mínimo e máximo de uma janela ou widget para restringir as dimensões dentro de certos limites.
   
2. **Redimensionamento Automático**:
   - É possível configurar a janela para se ajustar automaticamente ao conteúdo que ela contém.
   
3. **Layouts**:
   - Os layouts são usados para organizar widgets dentro de uma janela e permitir que eles se redimensionem de maneira adequada quando a janela é redimensionada.

### Métodos Comuns
- `setMinimumSize(width, height)`: Define o tamanho mínimo da janela.
- `setMaximumSize(width, height)`: Define o tamanho máximo da janela.
- `resize(width, height)`: Redimensiona a janela para as dimensões especificadas.
- `setFixedSize(width, height)`: Define um tamanho fixo para a janela.

### Exemplo de Código: Configurando Tamanhos da Janela
Aqui está um exemplo que demonstra como configurar os tamanhos da janela em PySide:

```python
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configurações da janela
        self.setWindowTitle("Configuração de Tamanho da Janela")
        self.setGeometry(100, 100, 800, 600)  # Define a posição e o tamanho inicial da janela

        # Definindo tamanhos mínimos e máximos
        self.setMinimumSize(400, 300)
        self.setMaximumSize(1024, 768)

        # Rótulo de exemplo
        label = QLabel("Ajuste o tamanho da janela", self)
        label.setGeometry(200, 250, 400, 100)
        label.setAlignment(Qt.AlignCenter)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())
```

### Explicação do Código
1. **Importações**:
   - `from PySide6.QtWidgets import QApplication, QMainWindow, QLabel`: Importa as classes necessárias do módulo QtWidgets do PySide6.
   
2. **Classe Principal da Janela**:
   - `class MainWindow(QMainWindow)`: Define uma classe MainWindow que herda de QMainWindow.
   
3. **Inicialização da Janela**:
   - `self.setWindowTitle("Configuração de Tamanho da Janela")`: Define o título da janela.
   - `self.setGeometry(100, 100, 800, 600)`: Define a posição e o tamanho inicial da janela.
   
4. **Definindo Tamanhos Mínimos e Máximos**:
   - `self.setMinimumSize(400, 300)`: Define o tamanho mínimo da janela.
   - `self.setMaximumSize(1024, 768)`: Define o tamanho máximo da janela.
   
5. **Adicionando um Rótulo**:
   - `label = QLabel("Ajuste o tamanho da janela", self)`: Cria um rótulo e o adiciona à janela principal.
   - `label.setGeometry(200, 250, 400, 100)`: Define a posição e o tamanho do rótulo dentro da janela.
   - `label.setAlignment(Qt.AlignCenter)`: Centraliza o texto do rótulo.

### Conclusão
Configurar o tamanho da janela é uma parte fundamental do design de interfaces de usuário. Com PySide, você tem controle total sobre as dimensões das janelas e widgets, permitindo criar interfaces ajustáveis e responsivas conforme necessário. Usando os métodos apropriados, você pode garantir que sua aplicação ofereça uma experiência de usuário ideal, independentemente do tamanho da janela.

## 04) IMAGENS E CORES NA JANELA
Adicionar imagens e cores à interface do usuário pode melhorar significativamente a experiência visual da aplicação. Com PySide, você pode facilmente adicionar imagens e definir cores para widgets e janelas.

### Conceitos Principais
1. **Imagens**:
   - Você pode carregar e exibir imagens em widgets usando a classe `QLabel` com o método `setPixmap`.
   
2. **Cores**:
   - As cores podem ser definidas usando estilosheets ou diretamente através de métodos como `setStyleSheet` para widgets.
   - Cores podem ser aplicadas ao fundo da janela ou a widgets individuais.

### Exemplo de Código: Adicionando Imagens e Cores
Aqui está um exemplo que demonstra como adicionar imagens e definir cores para uma janela e seus widgets usando PySide:

```python
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QPixmap, QColor, QPalette

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configurações da janela
        self.setWindowTitle("Imagens e Cores na Janela")
        self.setGeometry(100, 100, 800, 600)  # Define a posição e o tamanho inicial da janela

        # Definindo a cor de fundo da janela
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("lightblue"))
        self.setPalette(palette)

        # Adicionando uma imagem
        label_image = QLabel(self)
        pixmap = QPixmap("path/to/your/image.jpg")  # Substitua pelo caminho da sua imagem
        label_image.setPixmap(pixmap)
        label_image.setGeometry(50, 50, pixmap.width(), pixmap.height())

        # Adicionando um rótulo com cor de fundo
        label_text = QLabel("Texto com fundo colorido", self)
        label_text.setGeometry(50, 300, 200, 50)
        label_text.setStyleSheet("background-color: yellow; color: red; font-size: 20px;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())
```

### Explicação do Código
1. **Importações**:
   - `from PySide6.QtWidgets import QApplication, QMainWindow, QLabel`: Importa as classes necessárias do módulo QtWidgets do PySide6.
   - `from PySide6.QtGui import QPixmap, QColor, QPalette`: Importa classes para manipulação de imagens e cores.

2. **Classe Principal da Janela**:
   - `class MainWindow(QMainWindow)`: Define uma classe MainWindow que herda de QMainWindow.

3. **Inicialização da Janela**:
   - `self.setWindowTitle("Imagens e Cores na Janela")`: Define o título da janela.
   - `self.setGeometry(100, 100, 800, 600)`: Define a posição e o tamanho inicial da janela.

4. **Definindo a Cor de Fundo da Janela**:
   - `self.setAutoFillBackground(True)`: Permite o preenchimento do fundo da janela.
   - `palette = self.palette()`: Obtém a paleta de cores atual da janela.
   - `palette.setColor(QPalette.Window, QColor("lightblue"))`: Define a cor de fundo da janela como azul claro.
   - `self.setPalette(palette)`: Aplica a paleta à janela.

5. **Adicionando uma Imagem**:
   - `label_image = QLabel(self)`: Cria um rótulo para exibir a imagem.
   - `pixmap = QPixmap("path/to/your/image.jpg")`: Carrega a imagem a partir do caminho especificado (substitua pelo caminho da sua imagem).
   - `label_image.setPixmap(pixmap)`: Define o pixmap (imagem) no rótulo.
   - `label_image.setGeometry(50, 50, pixmap.width(), pixmap.height())`: Define a posição e o tamanho do rótulo com a imagem.

6. **Adicionando um Rótulo com Cor de Fundo**:
   - `label_text = QLabel("Texto com fundo colorido", self)`: Cria um rótulo com texto.
   - `label_text.setGeometry(50, 300, 200, 50)`: Define a posição e o tamanho do rótulo.
   - `label_text.setStyleSheet("background-color: yellow; color: red; font-size: 20px;")`: Define a cor de fundo (amarelo), a cor do texto (vermelho) e o tamanho da fonte (20px) usando uma folha de estilo.

### Conclusão
Trabalhar com imagens e cores no PySide é uma maneira poderosa de melhorar a estética e a usabilidade da sua aplicação. Usando `QLabel` para exibir imagens e estilosheets para definir cores, você pode criar interfaces de usuário visualmente atraentes e intuitivas. Experimente diferentes combinações de imagens e cores para encontrar a melhor aparência para sua aplicação.

## 05) CAMPO DE TEXTO, CAMPO DE SENHA E PLACEHOLDER
Em PySide, você pode criar campos de texto e campos de senha utilizando a classe `QLineEdit`. Os placeholders são úteis para fornecer dicas visuais aos usuários sobre o que eles devem inserir em um campo específico.

### Conceitos Principais
1. **Campo de Texto**:
   - Usando `QLineEdit`, você pode criar um campo de entrada de texto.
   
2. **Campo de Senha**:
   - Um campo de senha também pode ser criado com `QLineEdit`, mas com o modo de exibição de senha habilitado.
   
3. **Placeholder**:
   - O placeholder é um texto que aparece no campo de entrada quando ele está vazio, fornecendo uma dica do que o usuário deve inserir.

### Exemplo de Código: Campo de Texto, Campo de Senha e Placeholder
Aqui está um exemplo que demonstra como criar um campo de texto, um campo de senha e definir placeholders em PySide:

```python
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Campos de Texto e Senha com Placeholders")
        self.setGeometry(100, 100, 400, 200)  # Define a posição e o tamanho inicial da janela

        # Widget principal
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        # Layout
        layout = QVBoxLayout(main_widget)

        # Campo de texto
        text_field = QLineEdit(self)
        text_field.setPlaceholderText("Digite seu nome")
        layout.addWidget(text_field)

        # Campo de senha
        password_field = QLineEdit(self)
        password_field.setPlaceholderText("Digite sua senha")
        password_field.setEchoMode(QLineEdit.Password)  # Modo de exibição de senha
        layout.addWidget(password_field)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
```

### Explicação do Código
1. **Importações**:
   - `from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget`: Importa as classes necessárias do módulo QtWidgets do PySide6.

2. **Classe Principal da Janela**:
   - `class MainWindow(QMainWindow)`: Define uma classe MainWindow que herda de QMainWindow.

3. **Inicialização da Janela**:
   - `self.setWindowTitle("Campos de Texto e Senha com Placeholders")`: Define o título da janela.
   - `self.setGeometry(100, 100, 400, 200)`: Define a posição e o tamanho inicial da janela.

4. **Widget Principal e Layout**:
   - `main_widget = QWidget(self)`: Cria o widget principal.
   - `self.setCentralWidget(main_widget)`: Define o widget principal como o widget central da janela.
   - `layout = QVBoxLayout(main_widget)`: Cria um layout vertical para organizar os widgets dentro do widget principal.

5. **Campo de Texto**:
   - `text_field = QLineEdit(self)`: Cria um campo de entrada de texto.
   - `text_field.setPlaceholderText("Digite seu nome")`: Define o placeholder para o campo de texto.
   - `layout.addWidget(text_field)`: Adiciona o campo de texto ao layout.

6. **Campo de Senha**:
   - `password_field = QLineEdit(self)`: Cria um campo de entrada de texto para a senha.
   - `password_field.setPlaceholderText("Digite sua senha")`: Define o placeholder para o campo de senha.
   - `password_field.setEchoMode(QLineEdit.Password)`: Define o modo de exibição para o campo de senha, que oculta os caracteres digitados.
   - `layout.addWidget(password_field)`: Adiciona o campo de senha ao layout.

### Conclusão
Utilizando `QLineEdit` para criar campos de texto e de senha com placeholders, você pode criar interfaces de usuário mais amigáveis e intuitivas. Os placeholders ajudam a orientar os usuários sobre o tipo de informação esperada em cada campo, enquanto os campos de senha garantem a privacidade das informações inseridas. Experimente personalizar os placeholders e as configurações dos campos para se adequar às necessidades da sua aplicação.

## 06) BOTÕES E CAIXA DE MENSAGEM
Em PySide, você pode criar botões interativos usando a classe `QPushButton` e exibir mensagens ao usuário com a classe `QMessageBox`. Esses componentes são essenciais para criar interfaces de usuário interativas e responsivas.

### Conceitos Principais
1. **Botões (`QPushButton`)**:
   - `QPushButton` é usado para criar botões clicáveis.
   - Você pode conectar o sinal de clique do botão a uma função que será executada quando o botão for clicado.

2. **Caixa de Mensagem (`QMessageBox`)**:
   - `QMessageBox` é usado para exibir mensagens informativas, de aviso, de erro, etc.
   - Pode ser configurada para exibir diferentes tipos de botões e ícones.

### Exemplo de Código: Botões e Caixa de Mensagem
Aqui está um exemplo que demonstra como criar botões e exibir caixas de mensagem em PySide:

```python
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Botões e Caixa de Mensagem")
        self.setGeometry(100, 100, 300, 200)  # Define a posição e o tamanho inicial da janela

        # Widget principal
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        # Layout
        layout = QVBoxLayout(main_widget)

        # Botão de Informação
        info_button = QPushButton("Mostrar Informação", self)
        info_button.clicked.connect(self.show_info_message)
        layout.addWidget(info_button)

        # Botão de Aviso
        warning_button = QPushButton("Mostrar Aviso", self)
        warning_button.clicked.connect(self.show_warning_message)
        layout.addWidget(warning_button)

        # Botão de Erro
        error_button = QPushButton("Mostrar Erro", self)
        error_button.clicked.connect(self.show_error_message)
        layout.addWidget(error_button)

    def show_info_message(self):
        QMessageBox.information(self, "Informação", "Esta é uma mensagem informativa.")

    def show_warning_message(self):
        QMessageBox.warning(self, "Aviso", "Esta é uma mensagem de aviso.")

    def show_error_message(self):
        QMessageBox.critical(self, "Erro", "Esta é uma mensagem de erro.")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
```

### Explicação do Código
1. **Importações**:
   - `from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QVBoxLayout, QWidget`: Importa as classes necessárias do módulo QtWidgets do PySide6.

2. **Classe Principal da Janela**:
   - `class MainWindow(QMainWindow)`: Define uma classe MainWindow que herda de QMainWindow.

3. **Inicialização da Janela**:
   - `self.setWindowTitle("Botões e Caixa de Mensagem")`: Define o título da janela.
   - `self.setGeometry(100, 100, 300, 200)`: Define a posição e o tamanho inicial da janela.

4. **Widget Principal e Layout**:
   - `main_widget = QWidget(self)`: Cria o widget principal.
   - `self.setCentralWidget(main_widget)`: Define o widget principal como o widget central da janela.
   - `layout = QVBoxLayout(main_widget)`: Cria um layout vertical para organizar os widgets dentro do widget principal.

5. **Botões**:
   - `info_button = QPushButton("Mostrar Informação", self)`: Cria um botão de informação.
   - `info_button.clicked.connect(self.show_info_message)`: Conecta o sinal de clique do botão à função `show_info_message`.
   - `layout.addWidget(info_button)`: Adiciona o botão ao layout.
   - `warning_button` e `error_button` são criados e configurados de forma similar, mas conectados às funções `show_warning_message` e `show_error_message`, respectivamente.

6. **Funções de Mensagem**:
   - `def show_info_message(self):`: Define a função `show_info_message` que exibe uma caixa de mensagem informativa.
   - `QMessageBox.information(self, "Informação", "Esta é uma mensagem informativa.")`: Exibe uma caixa de mensagem informativa.
   - `show_warning_message` e `show_error_message` são definidos de forma similar, mas exibem caixas de mensagem de aviso e de erro, respectivamente.

### Conclusão
Usando `QPushButton` para criar botões interativos e `QMessageBox` para exibir mensagens ao usuário, você pode criar interfaces de usuário ricas e informativas em PySide. Essas ferramentas permitem que você forneça feedback instantâneo aos usuários, melhorando a usabilidade e a experiência do usuário em suas aplicações. Experimente personalizar as mensagens e os botões para se adequar às necessidades específicas da sua aplicação.

## 07) CRIANDO A TELA DE LOGIN
Uma tela de login é uma interface comum em muitas aplicações que requerem autenticação de usuários. Vamos criar uma tela de login simples utilizando PySide6. Essa tela incluirá campos de texto para o nome de usuário e a senha, além de botões para "Entrar" e "Cancelar".

### Conceitos Principais
1. **Campos de Texto**:
   - `QLineEdit` é usado para criar campos de texto.
   - O modo de exibição do campo de senha pode ser configurado para ocultar a entrada do usuário.

2. **Botões**:
   - `QPushButton` é usado para criar botões clicáveis.

3. **Layout**:
   - `QVBoxLayout` e `QHBoxLayout` são usados para organizar os widgets verticalmente e horizontalmente.

### Exemplo de Código: Tela de Login
Aqui está um exemplo que demonstra como criar uma tela de login com PySide:

```python
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QMessageBox

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tela de Login")
        self.setGeometry(100, 100, 300, 200)  # Define a posição e o tamanho inicial da janela

        # Widget principal
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        # Layout principal
        main_layout = QVBoxLayout(main_widget)

        # Campo de texto para o nome de usuário
        self.username_label = QLabel("Nome de Usuário:")
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Digite seu nome de usuário")
        main_layout.addWidget(self.username_label)
        main_layout.addWidget(self.username_input)

        # Campo de texto para a senha
        self.password_label = QLabel("Senha:")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Digite sua senha")
        self.password_input.setEchoMode(QLineEdit.Password)  # Oculta a senha
        main_layout.addWidget(self.password_label)
        main_layout.addWidget(self.password_input)

        # Layout para os botões
        button_layout = QHBoxLayout()

        # Botão de Entrar
        self.login_button = QPushButton("Entrar")
        self.login_button.clicked.connect(self.handle_login)
        button_layout.addWidget(self.login_button)

        # Botão de Cancelar
        self.cancel_button = QPushButton("Cancelar")
        self.cancel_button.clicked.connect(self.close)  # Fecha a janela ao clicar em Cancelar
        button_layout.addWidget(self.cancel_button)

        main_layout.addLayout(button_layout)

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Aqui você pode adicionar a lógica de autenticação
        if username == "admin" and password == "password":
            QMessageBox.information(self, "Sucesso", "Login bem-sucedido!")
        else:
            QMessageBox.warning(self, "Erro", "Nome de usuário ou senha incorretos.")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = LoginWindow()
    window.show()

    sys.exit(app.exec())
```

### Explicação do Código
1. **Importações**:
   - `from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QMessageBox`: Importa as classes necessárias do módulo QtWidgets do PySide6.

2. **Classe Principal da Janela**:
   - `class LoginWindow(QMainWindow)`: Define uma classe LoginWindow que herda de QMainWindow.

3. **Inicialização da Janela**:
   - `self.setWindowTitle("Tela de Login")`: Define o título da janela.
   - `self.setGeometry(100, 100, 300, 200)`: Define a posição e o tamanho inicial da janela.

4. **Widget Principal e Layout Principal**:
   - `main_widget = QWidget(self)`: Cria o widget principal.
   - `self.setCentralWidget(main_widget)`: Define o widget principal como o widget central da janela.
   - `main_layout = QVBoxLayout(main_widget)`: Cria um layout vertical para organizar os widgets dentro do widget principal.

5. **Campos de Texto**:
   - `self.username_label = QLabel("Nome de Usuário:")`: Cria um rótulo para o campo de nome de usuário.
   - `self.username_input = QLineEdit()`: Cria um campo de texto para o nome de usuário.
   - `self.username_input.setPlaceholderText("Digite seu nome de usuário")`: Define um placeholder para o campo de nome de usuário.
   - `self.password_label = QLabel("Senha:")`: Cria um rótulo para o campo de senha.
   - `self.password_input = QLineEdit()`: Cria um campo de texto para a senha.
   - `self.password_input.setPlaceholderText("Digite sua senha")`: Define um placeholder para o campo de senha.
   - `self.password_input.setEchoMode(QLineEdit.Password)`: Configura o campo de senha para ocultar a entrada do usuário.

6. **Botões**:
   - `self.login_button = QPushButton("Entrar")`: Cria um botão de login.
   - `self.login_button.clicked.connect(self.handle_login)`: Conecta o sinal de clique do botão à função `handle_login`.
   - `self.cancel_button = QPushButton("Cancelar")`: Cria um botão de cancelar.
   - `self.cancel_button.clicked.connect(self.close)`: Conecta o sinal de clique do botão à função `close`, que fecha a janela.

7. **Função de Login**:
   - `def handle_login(self):`: Define a função `handle_login` que é chamada quando o botão de login é clicado.
   - `username = self.username_input.text()`: Obtém o texto do campo de nome de usuário.
   - `password = self.password_input.text()`: Obtém o texto do campo de senha.
   - `if username == "admin" and password == "password":`: Verifica se o nome de usuário e a senha estão corretos.
   - `QMessageBox.information(self, "Sucesso", "Login bem-sucedido!")`: Exibe uma mensagem de sucesso.
   - `QMessageBox.warning(self, "Erro", "Nome de usuário ou senha incorretos.")`: Exibe uma mensagem de erro se o nome de usuário ou a senha estiverem incorretos.

### Conclusão
Criar uma tela de login em PySide é bastante simples usando `QLineEdit` para campos de texto e `QPushButton` para botões. Combinando esses widgets com layouts verticais e horizontais, você pode organizar sua interface de forma clara e intuitiva. Experimente personalizar os textos e adicionar lógica de autenticação conforme necessário para atender às necessidades específicas da sua aplicação.

## 08) VALIDANDO LOGIN E SENHA
Para validar o login e a senha em uma aplicação, você precisará comparar os dados inseridos pelo usuário com os dados de login válidos. Abaixo, vou mostrar um exemplo simples de como validar um login e uma senha estática, bem como um exemplo de validação com dados de login armazenados em um banco de dados SQLite.

### Exemplo de Validação Simples
Neste exemplo, os dados de login válidos são definidos diretamente no código.

```python
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QMessageBox

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tela de Login")
        self.setGeometry(100, 100, 300, 200)  # Define a posição e o tamanho inicial da janela

        # Widget principal
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        # Layout principal
        main_layout = QVBoxLayout(main_widget)

        # Campo de texto para o nome de usuário
        self.username_label = QLabel("Nome de Usuário:")
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Digite seu nome de usuário")
        main_layout.addWidget(self.username_label)
        main_layout.addWidget(self.username_input)

        # Campo de texto para a senha
        self.password_label = QLabel("Senha:")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Digite sua senha")
        self.password_input.setEchoMode(QLineEdit.Password)  # Oculta a senha
        main_layout.addWidget(self.password_label)
        main_layout.addWidget(self.password_input)

        # Layout para os botões
        button_layout = QHBoxLayout()

        # Botão de Entrar
        self.login_button = QPushButton("Entrar")
        self.login_button.clicked.connect(self.handle_login)
        button_layout.addWidget(self.login_button)

        # Botão de Cancelar
        self.cancel_button = QPushButton("Cancelar")
        self.cancel_button.clicked.connect(self.close)  # Fecha a janela ao clicar em Cancelar
        button_layout.addWidget(self.cancel_button)

        main_layout.addLayout(button_layout)

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Verifica se os dados de login são válidos
        if self.validate_credentials(username, password):
            QMessageBox.information(self, "Sucesso", "Login bem-sucedido!")
        else:
            QMessageBox.warning(self, "Erro", "Nome de usuário ou senha incorretos.")

    def validate_credentials(self, username, password):
        # Dados de login válidos
        valid_username = "admin"
        valid_password = "password"

        # Verifica se os dados inseridos correspondem aos dados válidos
        return username == valid_username and password == valid_password

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = LoginWindow()
    window.show()

    sys.exit(app.exec())
```

### Exemplo de Validação com Banco de Dados SQLite
Neste exemplo, os dados de login válidos são armazenados em um banco de dados SQLite.

```python
import sys
import sqlite3
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QMessageBox

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tela de Login")
        self.setGeometry(100, 100, 300, 200)  # Define a posição e o tamanho inicial da janela

        # Widget principal
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        # Layout principal
        main_layout = QVBoxLayout(main_widget)

        # Campo de texto para o nome de usuário
        self.username_label = QLabel("Nome de Usuário:")
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Digite seu nome de usuário")
        main_layout.addWidget(self.username_label)
        main_layout.addWidget(self.username_input)

        # Campo de texto para a senha
        self.password_label = QLabel("Senha:")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Digite sua senha")
        self.password_input.setEchoMode(QLineEdit.Password)  # Oculta a senha
        main_layout.addWidget(self.password_label)
        main_layout.addWidget(self.password_input)

        # Layout para os botões
        button_layout = QHBoxLayout()

        # Botão de Entrar
        self.login_button = QPushButton("Entrar")
        self.login_button.clicked.connect(self.handle_login)
        button_layout.addWidget(self.login_button)

        # Botão de Cancelar
        self.cancel_button = QPushButton("Cancelar")
        self.cancel_button.clicked.connect(self.close)  # Fecha a janela ao clicar em Cancelar
        button_layout.addWidget(self.cancel_button)

        main_layout.addLayout(button_layout)

        # Cria a tabela de usuários se não existir
        self.create_user_table()

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Verifica se os dados de login são válidos
        if self.validate_credentials(username, password):
            QMessageBox.information(self, "Sucesso", "Login bem-sucedido!")
        else:
            QMessageBox.warning(self, "Erro", "Nome de usuário ou senha incorretos.")

    def create_user_table(self):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()
        cursor.execute('INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)', ('admin', 'password'))
        conn.commit()
        conn.close()

    def validate_credentials(self, username, password):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        result = cursor.fetchone()
        conn.close()
        return result is not None

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = LoginWindow()
    window.show()

    sys.exit(app.exec())
```

### Explicação do Código
#### Validação Simples
1. **Dados de Login Válidos**:
   - Definidos diretamente no código (`valid_username` e `valid_password`).

2. **Função de Validação**:
   - `validate_credentials`: Compara os dados inseridos pelo usuário com os dados válidos.

#### Validação com Banco de Dados SQLite
1. **Banco de Dados**:
   - Um banco de dados SQLite é usado para armazenar os dados de login.

2. **Criação da Tabela de Usuários**:
   - `create_user_table`: Cria a tabela `users` se ela não existir e insere um usuário padrão (`admin`, `password`).

3. **Função de Validação**:
   - `validate_credentials`: Consulta o banco de dados para verificar se os dados inseridos pelo usuário são válidos.

Esses exemplos demonstram duas maneiras de validar o login e a senha do usuário em uma aplicação PySide. A primeira abordagem é adequada para casos simples ou demonstrações, enquanto a segunda abordagem é mais adequada para aplicações reais que exigem persistência de dados.

## 09) ABRINDO A SEGUNDA JANELA
Para abrir uma segunda janela após um login bem-sucedido, você pode criar uma nova classe que represente essa segunda janela e instanciá-la quando o login for validado com sucesso. Vou adicionar um exemplo de como abrir uma segunda janela após a validação do login, utilizando a estrutura do código de validação de login com banco de dados SQLite.

### Código Completo com a Segunda Janela
```python
import sys
import sqlite3
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QMessageBox

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tela de Login")
        self.setGeometry(100, 100, 300, 200)

        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        main_layout = QVBoxLayout(main_widget)

        self.username_label = QLabel("Nome de Usuário:")
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Digite seu nome de usuário")
        main_layout.addWidget(self.username_label)
        main_layout.addWidget(self.username_input)

        self.password_label = QLabel("Senha:")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Digite sua senha")
        self.password_input.setEchoMode(QLineEdit.Password)
        main_layout.addWidget(self.password_label)
        main_layout.addWidget(self.password_input)

        button_layout = QHBoxLayout()

        self.login_button = QPushButton("Entrar")
        self.login_button.clicked.connect(self.handle_login)
        button_layout.addWidget(self.login_button)

        self.cancel_button = QPushButton("Cancelar")
        self.cancel_button.clicked.connect(self.close)
        button_layout.addWidget(self.cancel_button)

        main_layout.addLayout(button_layout)

        self.create_user_table()

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if self.validate_credentials(username, password):
            QMessageBox.information(self, "Sucesso", "Login bem-sucedido!")
            self.open_main_window()
        else:
            QMessageBox.warning(self, "Erro", "Nome de usuário ou senha incorretos.")

    def create_user_table(self):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()
        cursor.execute('INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)', ('admin', 'password'))
        conn.commit()
        conn.close()

    def validate_credentials(self, username, password):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        result = cursor.fetchone()
        conn.close()
        return result is not None

    def open_main_window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Janela Principal")
        self.setGeometry(100, 100, 400, 300)

        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        main_layout = QVBoxLayout(main_widget)

        welcome_label = QLabel("Bem-vindo à Janela Principal!")
        main_layout.addWidget(welcome_label)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    login_window = LoginWindow()
    login_window.show()

    sys.exit(app.exec())
```

### Explicação do Código
#### Classe `LoginWindow`
1. **LoginWindow**: A janela principal onde o usuário insere o nome de usuário e a senha.
2. **handle_login**: Verifica as credenciais e, se forem válidas, abre a segunda janela (MainWindow) e fecha a janela de login.
3. **open_main_window**: Método que cria e mostra a `MainWindow`.

#### Classe `MainWindow`
1. **MainWindow**: Representa a segunda janela que é aberta após um login bem-sucedido.
2. **Layout e Widgets**: Contém uma simples mensagem de boas-vindas.

### Fluxo de Funcionamento
1. O usuário insere o nome de usuário e a senha na `LoginWindow`.
2. Ao clicar em "Entrar", o método `handle_login` verifica as credenciais.
3. Se as credenciais forem válidas, o método `open_main_window` é chamado.
4. `open_main_window` instancia a `MainWindow` e a exibe, enquanto a `LoginWindow` é fechada.

Com esse exemplo, você pode abrir uma segunda janela após validar o login, proporcionando uma navegação entre janelas na sua aplicação PySide.

## 10) CONFIGURANDO A JANELA PRINCIPAL
Para configurar a janela principal com mais detalhes e funcionalidades, podemos adicionar alguns elementos de interface, como menus, barras de ferramentas e status bar. Abaixo, vou mostrar como configurar uma janela principal mais completa utilizando PySide6.

### Configurando a Janela Principal
Vamos adicionar um menu, uma barra de ferramentas e uma barra de status à nossa janela principal. Além disso, vamos criar algumas ações para os menus e botões da barra de ferramentas.

### Código Completo
```python
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QAction, QMenu, QToolBar, QStatusBar
from PySide6.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Janela Principal Configurada")
        self.setGeometry(100, 100, 800, 600)

        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        main_layout = QVBoxLayout(main_widget)

        self.welcome_label = QLabel("Bem-vindo à Janela Principal Configurada!")
        main_layout.addWidget(self.welcome_label)

        self.create_menu()
        self.create_toolbar()
        self.create_statusbar()

    def create_menu(self):
        # Criação da barra de menu
        menubar = self.menuBar()

        # Menu Arquivo
        file_menu = menubar.addMenu("Arquivo")

        # Ação Abrir
        open_action = QAction(QIcon('open.png'), 'Abrir', self)
        open_action.setStatusTip('Abrir um arquivo')
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        # Ação Sair
        exit_action = QAction(QIcon('exit.png'), 'Sair', self)
        exit_action.setStatusTip('Sair do aplicativo')
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Menu Ajuda
        help_menu = menubar.addMenu("Ajuda")

        # Ação Sobre
        about_action = QAction(QIcon('about.png'), 'Sobre', self)
        about_action.setStatusTip('Informações sobre o aplicativo')
        about_action.triggered.connect(self.about)
        help_menu.addAction(about_action)

    def create_toolbar(self):
        # Criação da barra de ferramentas
        toolbar = QToolBar("Minha Barra de Ferramentas")
        self.addToolBar(toolbar)

        # Ação Abrir
        open_action = QAction(QIcon('open.png'), 'Abrir', self)
        open_action.setStatusTip('Abrir um arquivo')
        open_action.triggered.connect(self.open_file)
        toolbar.addAction(open_action)

        # Ação Sair
        exit_action = QAction(QIcon('exit.png'), 'Sair', self)
        exit_action.setStatusTip('Sair do aplicativo')
        exit_action.triggered.connect(self.close)
        toolbar.addAction(exit_action)

    def create_statusbar(self):
        # Criação da barra de status
        statusbar = QStatusBar()
        self.setStatusBar(statusbar)
        statusbar.showMessage('Pronto')

    def open_file(self):
        print("Ação Abrir executada")

    def about(self):
        print("Ação Sobre executada")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())
```

### Explicação do Código
#### Estrutura da Classe `MainWindow`
1. **Inicialização**:
    - `self.setWindowTitle("Janela Principal Configurada")`: Define o título da janela.
    - `self.setGeometry(100, 100, 800, 600)`: Define a posição e o tamanho da janela.

2. **Widgets Centrais**:
    - `QVBoxLayout`: Layout vertical para organizar os widgets no widget central.
    - `QLabel`: Um rótulo de boas-vindas na janela principal.

3. **Criação de Menu**:
    - `menuBar()`: Obtém a barra de menus da janela.
    - `QMenu`: Cria menus como "Arquivo" e "Ajuda".
    - `QAction`: Define ações como "Abrir", "Sair" e "Sobre", com ícones, dicas de status e conexões de sinal para os métodos correspondentes.

4. **Barra de Ferramentas**:
    - `QToolBar`: Cria uma barra de ferramentas com ações semelhantes às do menu.

5. **Barra de Status**:
    - `QStatusBar`: Cria uma barra de status que exibe mensagens de status.

6. **Métodos de Ações**:
    - `open_file`: Método de exemplo para a ação "Abrir".
    - `about`: Método de exemplo para a ação "Sobre".

### Personalização
- **Ícones**: Você pode adicionar ícones personalizados para as ações substituindo `'open.png'`, `'exit.png'`, etc.
- **Métodos de Ação**: Atualize os métodos `open_file` e `about` com a lógica necessária para o seu aplicativo.

Com essa configuração, sua janela principal terá uma barra de menu, uma barra de ferramentas e uma barra de status, proporcionando uma interface de usuário mais rica e interativa.

## 11) CONSTRUINDO E GERENCIANDO OS FRAMES
Construir e gerenciar frames em PySide6 envolve a criação de widgets que atuam como contêineres para organizar e agrupar outros widgets. Frames são úteis para dividir a interface em seções distintas, facilitando a organização e a estruturação do layout da aplicação. Abaixo, vou explicar como construir e gerenciar frames em PySide6, usando exemplos práticos.

### Construção de Frames
Para construir um frame em PySide6, você utiliza a classe `QFrame` que faz parte do módulo `QtWidgets`. Aqui está um exemplo básico de como criar e adicionar um frame à janela principal:

```python
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QFrame

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exemplo de Frames")
        self.setGeometry(100, 100, 600, 400)

        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        main_layout = QVBoxLayout(main_widget)

        # Criando um frame
        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)  # Define o estilo do frame
        frame_layout = QVBoxLayout(frame)

        # Adicionando widgets ao frame
        label1 = QLabel("Este é o Frame 1")
        button1 = QPushButton("Botão no Frame 1")
        frame_layout.addWidget(label1)
        frame_layout.addWidget(button1)

        # Adicionando o frame ao layout principal da janela
        main_layout.addWidget(frame)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
```

### Explicação do Código
1. **Inicialização da Janela (`MainWindow`)**:
   - `super().__init__()`: Chama o construtor da classe pai (QMainWindow).
   - `self.setWindowTitle("Exemplo de Frames")`: Define o título da janela.
   - `self.setGeometry(100, 100, 600, 400)`: Define a posição e o tamanho da janela.

2. **Widget Central**:
   - `QWidget`: Cria um widget central para a aplicação.
   - `self.setCentralWidget(main_widget)`: Define o widget central da janela como `main_widget`.

3. **Layout Principal (`QVBoxLayout`)**:
   - `QVBoxLayout`: Cria um layout vertical para organizar widgets no widget central (`main_widget`).

4. **Criação e Configuração do Frame (`QFrame`)**:
   - `QFrame`: Cria um frame para agrupar widgets.
   - `frame.setFrameShape(QFrame.StyledPanel)`: Define o estilo do frame como um painel estilizado.
   - `frame_layout`: Cria um layout vertical dentro do frame (`QVBoxLayout(frame)`).

5. **Adição de Widgets ao Frame**:
   - `QLabel` e `QPushButton`: Cria widgets para serem adicionados ao frame.
   - `frame_layout.addWidget(label1)`: Adiciona o rótulo ao layout do frame.
   - `frame_layout.addWidget(button1)`: Adiciona o botão ao layout do frame.

6. **Adição do Frame ao Layout Principal**:
   - `main_layout.addWidget(frame)`: Adiciona o frame ao layout principal da janela.

### Gerenciamento de Frames
Para gerenciar múltiplos frames ou alternar entre eles dinamicamente, você pode usar métodos para adicionar, remover ou esconder frames conforme necessário. Aqui está um exemplo básico de como alternar entre dois frames:

```python
# Exemplo de alternância entre frames

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Alternância de Frames")
        self.setGeometry(100, 100, 600, 400)

        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        self.frame1 = QFrame()
        self.frame1.setFrameShape(QFrame.StyledPanel)
        self.frame1_layout = QVBoxLayout(self.frame1)
        self.label1 = QLabel("Este é o Frame 1")
        self.button_to_frame2 = QPushButton("Ir para o Frame 2")
        self.frame1_layout.addWidget(self.label1)
        self.frame1_layout.addWidget(self.button_to_frame2)

        self.frame2 = QFrame()
        self.frame2.setFrameShape(QFrame.StyledPanel)
        self.frame2_layout = QVBoxLayout(self.frame2)
        self.label2 = QLabel("Este é o Frame 2")
        self.button_to_frame1 = QPushButton("Ir para o Frame 1")
        self.frame2_layout.addWidget(self.label2)
        self.frame2_layout.addWidget(self.button_to_frame1)

        self.current_frame = None
        self.show_frame(self.frame1)

        self.button_to_frame2.clicked.connect(lambda: self.show_frame(self.frame2))
        self.button_to_frame1.clicked.connect(lambda: self.show_frame(self.frame1))

    def show_frame(self, frame):
        if self.current_frame:
            self.current_frame.hide()
        frame.show()
        self.current_frame = frame
```

### Explicação Adicional
- **Alternância entre Frames**:
  - `show_frame(self, frame)`: Método que oculta o frame atual e mostra o novo frame especificado. Isso permite alternar entre diferentes frames na mesma janela.

### Considerações Finais
Ao construir e gerenciar frames em PySide6, é importante organizar os widgets de forma estruturada, utilizando layouts adequados para garantir uma interface de usuário limpa e intuitiva. Além disso, você pode personalizar o estilo e o comportamento dos frames de acordo com as necessidades específicas da sua aplicação.

## 12) COLOCANDO OS ELEMENTOS NOS FRAMES CADASTRAR E PESQUISAR
Para colocar elementos nos frames "Cadastrar" e "Pesquisar" dentro da janela principal usando PySide6, você pode seguir uma abordagem similar à que foi apresentada anteriormente. Vamos criar dois frames separados e adicionar widgets relevantes a cada um deles.

### Exemplo: Colocando Elementos nos Frames "Cadastrar" e "Pesquisar"
Aqui está um exemplo de como você pode estruturar sua aplicação para incluir os frames "Cadastrar" e "Pesquisar" na janela principal:

```python
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QFrame, QLineEdit, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exemplo de Frames")
        self.setGeometry(100, 100, 600, 400)

        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        main_layout = QVBoxLayout(main_widget)

        # Frame de Cadastrar
        self.frame_cadastrar = QFrame()
        self.frame_cadastrar.setFrameShape(QFrame.StyledPanel)
        layout_cadastrar = QVBoxLayout(self.frame_cadastrar)
        
        label_nome = QLabel("Nome:")
        self.input_nome = QLineEdit()
        layout_cadastrar.addWidget(label_nome)
        layout_cadastrar.addWidget(self.input_nome)

        label_email = QLabel("Email:")
        self.input_email = QLineEdit()
        layout_cadastrar.addWidget(label_email)
        layout_cadastrar.addWidget(self.input_email)

        button_cadastrar = QPushButton("Cadastrar")
        layout_cadastrar.addWidget(button_cadastrar)
        
        main_layout.addWidget(self.frame_cadastrar)

        # Frame de Pesquisar
        self.frame_pesquisar = QFrame()
        self.frame_pesquisar.setFrameShape(QFrame.StyledPanel)
        layout_pesquisar = QVBoxLayout(self.frame_pesquisar)
        
        label_pesquisa = QLabel("Pesquisar por Nome:")
        self.input_pesquisa = QLineEdit()
        layout_pesquisar.addWidget(label_pesquisa)
        layout_pesquisar.addWidget(self.input_pesquisa)

        button_pesquisar = QPushButton("Pesquisar")
        layout_pesquisar.addWidget(button_pesquisar)

        main_layout.addWidget(self.frame_pesquisar)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
```

### Explicação do Código
1. **Janela Principal (`MainWindow`)**:
   - `super().__init__()`: Inicializa a classe QMainWindow.
   - `self.setWindowTitle("Exemplo de Frames")`: Define o título da janela.
   - `self.setGeometry(100, 100, 600, 400)`: Define a posição e o tamanho da janela.

2. **Widget Central**:
   - `QWidget`: Cria um widget central para a aplicação.
   - `self.setCentralWidget(main_widget)`: Define o widget central da janela como `main_widget`.

3. **Layout Principal (`QVBoxLayout`)**:
   - `QVBoxLayout`: Cria um layout vertical para organizar widgets no widget central (`main_widget`).

4. **Frame de Cadastrar (`frame_cadastrar`)**:
   - `QFrame`: Cria um frame para o formulário de cadastro.
   - `setFrameShape(QFrame.StyledPanel)`: Define o estilo do frame como um painel estilizado.
   - `layout_cadastrar`: Cria um layout vertical dentro do frame para organizar os widgets de cadastro.
   - `QLabel` e `QLineEdit`: Cria rótulos e campos de entrada para nome e email.
   - `QPushButton`: Cria um botão para cadastrar os dados.

5. **Adição de Widgets ao Layout Principal**:
   - `main_layout.addWidget(self.frame_cadastrar)`: Adiciona o frame de cadastrar ao layout principal da janela.

6. **Frame de Pesquisar (`frame_pesquisar`)**:
   - `QFrame`: Cria um frame para a pesquisa.
   - `setFrameShape(QFrame.StyledPanel)`: Define o estilo do frame como um painel estilizado.
   - `layout_pesquisar`: Cria um layout vertical dentro do frame para organizar os widgets de pesquisa.
   - `QLabel` e `QLineEdit`: Cria rótulos e campo de entrada para pesquisa por nome.
   - `QPushButton`: Cria um botão para realizar a pesquisa.

7. **Adição de Widgets ao Layout Principal**:
   - `main_layout.addWidget(self.frame_pesquisar)`: Adiciona o frame de pesquisar ao layout principal da janela.

### Funcionalidade Adicional
Para tornar a aplicação funcional, você precisará adicionar a lógica para capturar os dados dos campos de entrada e implementar ações como cadastro e pesquisa, dependendo dos requisitos do seu projeto. Além disso, você pode estilizar os widgets conforme necessário para melhorar a aparência e usabilidade da aplicação.

Este exemplo fornece uma estrutura básica para começar a trabalhar com frames, e você pode expandi-lo adicionando mais funcionalidades e personalizações conforme necessário.

## 13-14) MONTANDO A TABLEVIEW
Para montar uma `QTableView` em uma aplicação PySide6, você precisa seguir alguns passos básicos. A `QTableView` é usada para exibir dados tabulares, e você pode personalizá-la para mostrar e editar dados de diferentes maneiras. Abaixo está um exemplo básico de como você pode configurar uma `QTableView` dentro de uma janela principal usando PySide6:

### Exemplo de Como Montar uma TableView
```python
import sys
from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTableView, QPushButton


class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data
    
    def data(self, index: QModelIndex, role: int = ...):
        if role == Qt.DisplayRole:
            row = index.row()
            col = index.column()
            return self._data[row][col]
        return None
    
    def rowCount(self, parent: QModelIndex = ...) -> int:
        return len(self._data)
    
    def columnCount(self, parent: QModelIndex = ...) -> int:
        if self._data:
            return len(self._data[0])
        return 0


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exemplo de TableView")
        self.setGeometry(100, 100, 600, 400)

        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        main_layout = QVBoxLayout(main_widget)

        # Dados para a tabela
        data = [
            ["Alice", 25, "Feminino"],
            ["Bob", 30, "Masculino"],
            ["Charlie", 20, "Masculino"],
            ["Diana", 27, "Feminino"],
            ["Eve", 22, "Feminino"]
        ]

        # Modelo da tabela
        self.model = TableModel(data)

        # TableView
        self.table_view = QTableView()
        self.table_view.setModel(self.model)

        # Botão para atualizar dados (exemplo)
        self.update_button = QPushButton("Atualizar Dados")
        self.update_button.clicked.connect(self.atualizar_dados)

        main_layout.addWidget(self.table_view)
        main_layout.addWidget(self.update_button)

    def atualizar_dados(self):
        # Exemplo de atualização de dados na tabela
        new_data = [
            ["Alice", 25, "Feminino"],
            ["Bob", 30, "Masculino"],
            ["Charlie", 20, "Masculino"],
            ["David", 29, "Masculino"],
            ["Eve", 22, "Feminino"]
        ]
        self.model = TableModel(new_data)
        self.table_view.setModel(self.model)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
```

### Explicação do Código
1. **`QAbstractTableModel` (`TableModel`)**:
   - Uma classe personalizada derivada de `QAbstractTableModel` que define como os dados são exibidos e acessados na `QTableView`.
   - `data()`: Método para obter os dados a serem exibidos em uma célula específica da tabela.
   - `rowCount()` e `columnCount()`: Métodos para especificar o número de linhas e colunas na tabela.

2. **Janela Principal (`MainWindow`)**:
   - `QMainWindow`: Inicializa a janela principal da aplicação.
   - `setCentralWidget(main_widget)`: Define o widget central da janela como `main_widget`.

3. **Layout Principal (`QVBoxLayout`)**:
   - `QVBoxLayout`: Cria um layout vertical para organizar widgets no widget central (`main_widget`).

4. **Dados para a Tabela**:
   - `data`: Uma lista de listas que contém os dados a serem exibidos na tabela.

5. **Modelo da Tabela (`TableModel`)**:
   - `self.model`: Instância do modelo de tabela personalizado (`TableModel`) criado com os dados fornecidos.

6. **TableView (`QTableView`)**:
   - `self.table_view`: Instância de `QTableView` configurada com o modelo de tabela (`self.model`).

7. **Botão para Atualizar Dados**:
   - `self.update_button`: Um botão que, quando clicado, atualiza os dados exibidos na tabela com novos dados (`new_data`).

8. **Método `atualizar_dados()`**:
   - `atualizar_dados()`: Um método conectado ao botão de atualização que redefine o modelo da tabela com novos dados (`new_data`) e atualiza a `QTableView`.

### Funcionalidades Adicionais
- Você pode adicionar mais funcionalidades, como ordenação de colunas, edição de células, seleção de linhas e colunas, entre outras, conforme necessário.
- Personalize o modelo (`TableModel`) de acordo com a estrutura dos seus dados para garantir que a tabela exiba corretamente as informações desejadas.
- Explore as propriedades e métodos disponíveis em `QTableView` e `QAbstractTableModel` para mais opções de personalização e controle sobre a exibição e manipulação dos dados na tabela.

Este exemplo fornece uma estrutura básica para montar e atualizar uma `QTableView` em uma aplicação PySide6. Você pode expandir e modificar o código de acordo com os requisitos específicos do seu projeto.