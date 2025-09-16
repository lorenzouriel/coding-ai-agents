## SOLUTION 1: **Use `socat` with a public IP**
Since port `11434` is already in local use, we will **expose another port**, such as `9111`, which we redirect to `127.0.0.1:11434`.

###Step:
On machine **10.0.0.xxx**, I ran:
```bash
sudo socat TCP -LISTEN:9111,fork,reuseaddr TCP:127.0.0.1:11434

nohup sudo socat TCP -LISTEN:9111,fork,reuseaddr TCP:127.0.0.1:11434 > ~/socat.log 2>&1 &
```

Now, on the client machine, try:
```bash
curl http://10.0.0.xxx:9111
```

## SOLUTION 2: **Use the client machine's `ssh` tunnel**
If you have SSH access to machine `10.0.0.xxx`, run in your terminal (on the client machine):
```bash
ssh -L 11434:127.0.0.1:11434ubuntu@10.0.0.xxx
```

Then, **still on your machine**, run:
```bash
curl http://127.0.0.1:11434
```