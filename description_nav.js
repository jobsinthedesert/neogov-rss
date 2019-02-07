const fs = require('fs');
const path = require('path');
const puppeteer = require('puppeteer');

(async () => {
  //const browser = await puppeteer.launch({headless: false});
  const browser = await puppeteer.launch();
  const page = (await browser.pages())[0];
  await page.goto('https://www.governmentjobs.com/careers/sunline/jobs/2343766/bus-driver');


  const html = await page.content();
  
  
  /*
  await page.evaluate(() => {
    document.querySelector('.print-button').click();
  })
  */

  url = await page.evaluate(() => {
    return document.querySelector('.print-button').getAttribute('href')
  })

  await page.goto(url);
  
  //await page.emulateMedia('screen');
  await page.content();
  await page.pdf({path: 'web.pdf'});

  /*
  const file = path.join('output', 'dom.html');

  fs.writeFile(file, html, (err) => {
    if (err) throw err;
  });
  */

  

  await browser.close();

  
})();

/*

#main-container > div.content-container > div > div > div > div > div.container.entity-details-tab.active > div > div.header-buttons > a


Start-Process chrome -Verb Runas -Arg
umentList '--headless --disable-gpu --print-to-pdf="C:\jobsinthedesert_tools\parsers\
neogov-rss\test.pdf" "https://agency.governmentjobs.com/sunline/job_bulletin.cfm?jobI
D=2343766&sharedWindow=0"'


*/