
console.log('ClientAuth extension loaded')

function getInfo(req) {
    console.log(`Got request for ${req.url} with ID ${req.requestId}`)

    let securityInfo = browser.webRequest.getSecurityInfo(req.requestId, {
        certificateChain: true,
        rawDER: false
    });

    console.log(`securityInfo: ${JSON.stringify(securityInfo, null, 2)}`)
}

browser.webRequest.onHeadersReceived.addListener(
    getInfo,
    { urls: ['<all_urls>'] },
    ['blocking', 'responseHeaders']
)

console.log('Added listener')

