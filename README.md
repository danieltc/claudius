# claudius
sistema de rol de membros para igreja presbiteriana

#instalação

```
git clone https://github.com/danieltc/claudius.git
cd claudius/
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt 
cp ../db.sqlite3 .
python manage.py changepassword admin
python manage.py runserver --insecure
```

Se for no windows, a linha de ativar o venv é diferente:
```
# In cmd.exe
venv\Scripts\activate.bat
# In PowerShell
venv\Scripts\Activate.ps1
```

Quase todos os dados foram devidamente alterados para ocultar qualquer informação sensível. 
Vários dados um pouco mais sensíveis foram completamente removidos. 
Com isso, alguns relatórios não fazem sentido (todas as pessoas ficaram com a minha data de casamento, por exemplo)

Qualquer dúvida, me mande um email. danieltc@gmail.com

Infelizmente as tabelas de domínio NÃO foram convertidas em migrations quando criei o sistema, e é por isso que o banco está indo junto.
