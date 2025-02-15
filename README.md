# **Gerador de CSV - Campos Zendesk**

![Badge](https://img.shields.io/badge/Python-3.x-blue) ![Badge](https://img.shields.io/badge/CSV-Automation-green) ![Badge](https://img.shields.io/badge/Zendesk-Integration-orange)

## **📌 Descrição**
O **Gerador de CSV - Campos Zendesk** é uma ferramenta desenvolvida em Python que processa um arquivo CSV contendo nomes de campos de listas suspensas e gera um novo arquivo CSV formatado conforme o padrão exigido pelo **Zendesk**. O script ajusta os nomes das colunas, transforma os valores corretamente e define padrões específicos para os campos do novo CSV.

---

## **🛠 Funcionalidades**
✔️ Lê um arquivo CSV de entrada contendo os nomes dos campos da lista suspensa.  
✔️ Gera um novo arquivo CSV no formato exigido pelo Zendesk.  
✔️ Remove espaços e converte os valores para **minúsculas** no campo `tag`.  
✔️ Define o campo `default` sempre como `false`.  
✔️ Automatiza o processo de padronização, reduzindo erros manuais.  

---

## **📂 Estrutura do Projeto**
```
📂 Gerador-de-CSV---Campos-Zendesk
│── 📄 script.py            # Código principal para processar o CSV
│── 📄 requirements.txt      # Lista de dependências necessárias
│── 📄 modeloCSV.csv         # Modelo do CSV no formato correto
│── 📄 README.md             # Documentação do projeto
```

---

## **🚀 Como Usar**
### **1️⃣ Clonar o Repositório**
Abra o terminal e execute:
```sh
git clone https://github.com/italogax/Gerador-de-CSV---Campos-Zendesk.git
cd Gerador-de-CSV---Campos-Zendesk
```

### **2️⃣ Criar um Ambiente Virtual (Opcional)**
Para evitar conflitos de dependências, é recomendado criar um ambiente virtual:
```sh
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### **3️⃣ Instalar Dependências**
Execute o comando:
```sh
pip install -r requirements.txt
```

### **4️⃣ Executar o Script**
Para rodar o script, execute:
```sh
python script.py
```
Isso processará o CSV de entrada e gerará um novo arquivo formatado.

---

## **📊 Exemplo de Entrada e Saída**
### **📥 Entrada (arquivo CSV original)**
```
value
Opção 1
Opção 2
Opção 3
```

### **📤 Saída Gerada (arquivo CSV formatado)**
```
value,tag,default
Opção 1,opcao1,false
Opção 2,opcao2,false
Opção 3,opcao3,false
```

---

## **⚙️ Tecnologias Utilizadas**
- **Python** 🐍
- **Pandas** 📊
- **CSV Manipulation** 📑

---

## **📝 Licença**
Este projeto está licenciado sob a **MIT License** – consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## **📩 Contato**
🔹 Desenvolvido por [Italo Gax](https://github.com/italogax)  
📧 E-mail: italogax@example.com  

Se este projeto foi útil para você, deixe uma ⭐ no repositório! 🚀✨
