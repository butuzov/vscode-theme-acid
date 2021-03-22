# ACID

Code in Golang/Python/PHP with Darkish VSCode Theme

[![Marketplace](https://vsmarketplacebadge.apphb.com/version/butuzov.acid.svg)](https://marketplace.visualstudio.com/items/butuzov.acid) [![Installs](https://vsmarketplacebadge.apphb.com/installs/butuzov.acid.svg)](https://marketplace.visualstudio.com/items/butuzov.acid) [![Ratings](https://vsmarketplacebadge.apphb.com/rating-short/butuzov.acid.svg)](https://marketplace.visualstudio.com/items/butuzov.acid)

## Screenshots

![Main Page](./assets/acid_exp_page.png)
_Main Theme Page_

![Golang in ACID](./assets/acid_go.png)
_Editing Go with ACID_

![proto3 in ACID](./assets/acid_proto.png)
_Editing proto4 with ACID_

## Syntax Highlighting

Supported syntax highlighting: `Go`/`Golang` (and` Go` templates), `Python`, `Starlark`, `PHP`, `TypeScript`, `JavaScript`, `CSS`/`LESS`/`SCSS`, `Dockerfile`, `Markdown`, `protobuf`, `yaml`, `hcl`, `shell`.

## Contributing

We have to dead with 3 yaml files: `palette.yaml` - out pallet, `theme.yaml` - values for colors and `tokens.yaml` syntax coloring. If you are not familiar with it - checkout [Learn  in Y minutes](https://learnxinyminutes.com/docs/yaml/) entry for yaml.

Editing tokens - prefixes stands:
* `i` for italic
* `b` fod bold
* `u` for underline

```yaml
# example 1: theme.yaml
editor:
  background: black            # rgb value ref as black (see pallet.yaml)
  foreground: white/a90        # rgb value ref as white with 90% alpha (see pallet.yaml)

# example 2: tokens.yaml
formats:
  comment: &comment
    style: i@syntax.white/a50 # italic font and white text with 50% alpha (see pallet.yaml)
```

After changes done, you can recompile json. You can use either `make` or [`task`](https://github.com/go-task/task).

```shell
# continues recompile ... using make
make build
# continues recompile ... using task
task -w
```

## References

* [Hexadecimal color code for transparency](https://gist.github.com/lopspower/03fb1cc0ac9f32ef38f4)
* [vscode themes](https://vscodethemes.com/)
* [api theme colors](https://code.visualstudio.com/api/references/theme-color)
