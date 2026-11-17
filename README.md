# Terminal Cheat Code

Turn plain English into an executable shell command using **only a local Ollama model**. It makes requests exclusively to an Ollama server on your own computer and rejects remote hosts. There is no cloud AI provider, API key, telemetry, or runtime dependency outside Python's standard library.

## Requirements

- Python 3.9 or newer
- [Ollama](https://ollama.com) installed and running locally
- At least one Ollama model already downloaded to the machine

## Install from GitHub

```sh
git clone https://github.com/YOUR-USERNAME/terminal-cheat-code.git
cd terminal-cheat-code
ollama pull qwen2.5-coder:7b
python3 install.py
```

The installer uses only Python's standard library; it does not need `pip`, package downloads, or any third-party runtime dependency. It installs `cheat` to `~/.local/bin` on macOS/Linux and prints the `PATH` command if your terminal does not already find it. On Windows it installs a `cheat.cmd` launcher in the per-user Python Scripts directory.

Replace `qwen2.5-coder:7b` with any model you prefer; the CLI automatically uses the first locally installed model unless you choose one with `--model`.

To update after pulling a newer version, run:

```sh
python3 install.py --force
```

If Ollama is not already running, start it in a separate terminal:

```sh
ollama serve
```

Verify the installation:

```sh
cheat --version
cheat --help
```

## Use

```sh
cheat "how do I undo my last git commit but keep the changes"
cheat -m qwen2.5-coder:7b "show the 10 largest files in this directory"
cheat --set-model qwen2.5-coder:7b
cheat -c "archive all .log files older than 30 days"
cheat -e "create a Python virtual environment"
```

It detects your current shell, or select one explicitly:

```sh
cheat --shell fish "find every TypeScript file containing TODO"
```

The generated command is displayed but never executed unless you pass `--execute`; that mode still requires an interactive `y` confirmation. The `--copy` option copies it to your system clipboard.

## Configuration and privacy

`cheat --set-model MODEL` stores a default in `~/.terminal-cheat-code.json` with owner-only permissions. The optional `--host` flag supports another loopback Ollama endpoint, e.g. `http://localhost:11434`. Requests only target `HOST/api/chat`; `localhost`, `127.0.0.1`, and `::1` are the only accepted hosts.

## Development checks

Run the test suite from the cloned repository:

```sh
python3 -m unittest -v
```

Run `cheat --help` for every option.
