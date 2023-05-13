# trac-references-mail-decorator

This Trac plugin will add header's `Message-ID` field to `References` field.

## Background

Amazon SES changes header's `Message-ID` to its own format, which causes mail clients unable to identify the relation of threading.  (Mails from second mail have `References` field.)

This plugin implements an workaround.  It will copy `Message-ID` to `References` if no `References` field existed, therefore rebuild relationship between first mail and followings.

## Install

Only tested on Trac 1.4, but may work on Trac 1.2 since it uses `IEmailDecorator` only.

    pip install git+https://github.com/gslin/trac-references-mail-decorator.git

Then restart Trac and enable it from the admin interface.

## See also

https://github.com/weisslj/trac-messageid-plugin is also trying to solve this issue, with different approach.

## License

See [LICENSE](LICENSE) file.
