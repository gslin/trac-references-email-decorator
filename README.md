# trac-references-mail-decorator

This single file plugin for Trac will add header's `Message-ID` field to `References` field.

## Background

Amazon SES will change header's `Message-ID` to its own format, which causes mail clients unable to identify the first mail and other followings are in the same thread.  (Mails from second mail have `References` field.)

This plugin is a workaround plugin.  It will copy `Message-ID` to `References` if no `References` field existed, which rebuild relationship between first mail and other followings.

## Install

    pip install git+https://github.com/gslin/trac-references-mail-decorator.git

Then restart Trac and enable it from the admin interface.

## See also

https://github.com/weisslj/trac-messageid-plugin is also trying to solve this issue, with different approach.

## License

See [LICENSE](LICENSE) file.
