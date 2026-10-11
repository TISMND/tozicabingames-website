# Images

Empty for now — both game panels use CSS gradient placeholders.

To swap in real key art, drop the file here and point the matching
custom property in `styles.css` at it:

    --art-syntherion: url("img/syntherion.jpg");
    --art-third-party: url("img/the-third-party.jpg");

The panels use `background-size: cover`, so anything roughly 1600×1800
or larger will fill a half-screen panel on desktop without stretching.
