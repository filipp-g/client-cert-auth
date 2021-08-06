
console.log('ClientAuth extension loaded')

function getInfo(details) {
    console.log(`Got request for ${details.url} with ID ${details.requestId}`)

    var securityInfo = browser.webRequest.getSecurityInfo(details.requestId, {
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

