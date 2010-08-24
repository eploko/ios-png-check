# ios-png-check

A simple utility to check that your @2x iOS PNG assets targeting iPhone 4 are in a good shape.

Note: This is a ruby gem. If you want a Python version, you can find one in the `contrib/` folder. The Python version has been contributed by [Matt Galloway](http://iphone.galloway.me.uk/).

## How to Install

	$ gem update --system
	$ gem install ios-png-check

## How to Use

	$ cd folder-where-you-have-your-png-assets
	$ ios-png-check

## What it Does in Details

For each PNG image in the current folder it tries to find a @2x version and checks that the size of the @2x version is twice the size of the @1x version.

When done it outputs the summary of possible issues.

## Output Example

	FILES WITHOUT @1x VERSION ============================================
	status-new@2x.png

	FILES WITHOUT @2x VERSION ============================================
	Icon-Small.png
	logo.png
	message-bubble-left.png
	message-bubble-right.png
	no-photo-icon-boy-small.png
	no-photo-icon-girl-small.png
	nofriendsbg.png
	profile-gallery-super-star.png
	send-button.png
	share-on-network-bounds-rect.png

	INVALID IMAGE SIZES DETECTED FOR THE FOLLOWING FILES =================
	dashboard-checkin-button-full@2x.png: SIZE IS 506 x 94, EXPECTED 596 x 94

## Note on Patches/Pull Requests
 
* Fork the project.
* Make your feature addition or bug fix.
* Add tests for it. This is important so I don't break it in a
  future version unintentionally.
* Commit, do not mess with rakefile, version, or history.
  (if you want to have your own version, that is fine but bump version in a commit by itself I can ignore when I pull)
* Send me a pull request. Bonus points for topic branches.

## Copyright

Copyright (c) 2010 Andrey Subbotin. See LICENSE for details.
