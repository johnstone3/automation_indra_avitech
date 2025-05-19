ENCRYPTION_KEY := <placeholder>
ENCRYPTION_VALUE := <placeholder>

runTests:
	ENV_NAME=test SECRETS_DECRYPTION_KEY=$(ENCRYPTION_KEY) \
	poetry run pytest \
	--browser chromium \
	--slowmo 250 \
	--html="reports/report.html" \
	--self-contained-html

generateDecryptionKey:
	poetry run python -c "from cryptography.fernet import Fernet; key = Fernet.generate_key().decode(); print(key)"

encryptSecret:
	SECRETS_DECRYPTION_KEY=$(ENCRYPTION_KEY) \
	poetry run python -c \
	"import sys; import os; from cryptography.fernet import Fernet; key = os.environ['SECRETS_DECRYPTION_KEY']; f = Fernet(key.encode()); encrypted = f.encrypt(sys.argv[1].encode()).decode(); print(encrypted)" \
	"$(ENCRYPTION_VALUE)"

decryptSecret:
	SECRETS_DECRYPTION_KEY=$(ENCRYPTION_KEY) \
	poetry run python -c \
	"import sys; import os; from cryptography.fernet import Fernet; key = os.environ['SECRETS_DECRYPTION_KEY']; f = Fernet(key.encode()); decrypted = f.decrypt(sys.argv[1].encode()).decode(); print(decrypted)" \
	"$(ENCRYPTION_VALUE)"
