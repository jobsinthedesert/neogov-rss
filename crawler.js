const fs = require('fs');
const path = require('path');
const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({headless: false});
  const page = (await browser.pages())[0];
  await page.goto('https://www.governmentjobs.com/careers/sunline?');

  const html = await page.content();
  
  const file = path.join('output', 'dom.html');

  fs.writeFile(file, html, (err) => {
    if (err) throw err;
  });

  

  await browser.close();
})();

/*
Notes:

#action-grid-view
#action-list-view

http://agency.governmentjobs.com/sunline/job_bulletin.cfm?jobID=2343766&sharedWindow=0

*/