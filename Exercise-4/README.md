In this exercise I will experiment with GitHub Webhooks and configure the RabbitMQ message broker

I ran `npm install --global smee-client`

I started forwarding webhooks with this command `smee -u https://smee.io/uxxZGRJbuq2kyHMY --path /webhook --port 3000`

I ran `npm init` in github-hooks folder, then installed Express with `npm install express`

Then I started with the webhook server by cd into github-hooks folder, and running `node webhook-server.js`, making sure I had the forwarding webhooks up and running first in another terminal

For RabbitMQ, I installed it with `sudo apt install --yes rabbitmq-server`

I installed Pika with `python -m pip install pika --upgrade`

