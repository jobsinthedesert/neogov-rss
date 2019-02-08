$crawler_params = @(
    (".\crawler.js"),
    ("https://www.governmentjobs.com/careers/sunline?"),
    ("C:\jobsinthedesert_tools\parsers\neogov-rss\output\")
)

$parser_single_params = @(
    (".\parser_single.py"),
    ('-dom="C:\jobsinthedesert_tools\parsers\neogov-rss\output\dom.html"'),
    ('-output="C:\jobsinthedesert_tools\parsers\neogov-rss\output\jobs.xml"'),
    ('-title="Example neo-gov feed"'),
    ('-link="https://google.com"'),
    ('-log="C:\jobsinthedesert_tools\parsers\neogov-rss\output\parser.log"')
)

$link_grabber_params = @(
    (".\link_grabber.py"),
    ('-output_directory="C:\jobsinthedesert_tools\parsers\neogov-rss\output"')
    ('-feed_location="C:\jobsinthedesert_tools\parsers\neogov-rss\output\jobs.xml"')
)

node $crawler_params
python $parser_single_params
python $link_grabber_params

$counter = 0

$titles = Get-Content .\output\pdf_titles.txt
$output_dir = ".\output\"

foreach($link in Get-Content .\output\links.txt) {
    $pdf_title = $titles[$counter]

    $description_nav_params = @(
        (".\description_nav.js"),
        ($link),
        ($output_dir + $pdf_title)
    )

    node $description_nav_params

    $counter++
}

