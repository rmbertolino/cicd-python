# cicd-python
Example for CI/CD

Github Actions
* Plan gratuito incluye 2000 minutos de ejecucion de CICD

CI: Integración Continua (Testear y comprobar el linting)
* Test
python -m pytest

* Linting
ruff check .

CD: Despliegue Continuo (Desplegar en forma automática)
* Package
* deploy automático al VPS
* fake-vps
  * docker --version
  * docker run -d \
  --name fake-vps \
  --hostname fake-vps \
  -p 2222:22 \
  --restart unless-stopped \
  ubuntu:22.04 \
  sleep infinity
  * entrar al vps-fake
    * docker exec -it fake-vps bash