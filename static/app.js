var main = "man"
const api_url = `https://api.dictionaryapi.dev/api/v2/entries/en/${main}`;

async function getmeaning(url) {        
    let response = await fetch(url)
    let data = await response.json()
    // console.log(data)
    var naame= data[0].word
    var meaning = data[0].meanings
    console.log(naame)
    console.log(meaning[0].definitions[3].definition)

}

getmeaning(api_url);