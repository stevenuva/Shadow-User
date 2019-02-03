/*
* catalogue.js
* Javascript function to search books
* with the Google Books API
*/

window.onload= function bookSearch(){
    document.getElementById('results').innerHTML = ""
    var search = searchInput;
    console.log( document.getElementById('search').value)
    var apiKey="";
    var xmlhttp = new XMLHttpRequest();
    var url = "https://www.googleapis.com/books/v1/volumes?q=" + search +
    apiKey + "&langRestrict=en";

    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var data = JSON.parse(this.responseText);
            data.items.forEach(function(e,i) {
                var generatedUser = ['','',''];
                var image = "";
                if (data.items[i].volumeInfo.imageLinks !== undefined) {
                    image = data.items[i].volumeInfo.imageLinks.thumbnail
                }

                results.innerHTML += '<div class="col-md-12 mx-auto mb-1 rounded catalogueItems"><h2>' + data.items[i].volumeInfo.title + '</h2><img src="' + image + '"><p class="textCatalogue" ><strong>Author: </strong>' + data.items[i].volumeInfo.authors + '<br><strong>Category: </strong>'+ data.items[i].volumeInfo.categories +'<br><strong>Description: </strong>'+ data.items[i].volumeInfo.description + '</br><strong>Pages: </strong>'+ data.items[i].volumeInfo.pageCount + '</br><strong>Relevant Users:</strong></br><ul class="generatedUsersList"><li><h6 onclick="toggle_visibility' + "('userGen1')" + ';">' + generatedUser[0] + '</h6></li><li><h6 onclick="toggle_visibility' + "('userGen2')" + ';">' + generatedUser[0] + '</h6></li><li><h6 onclick="toggle_visibility' + "('userGen3')" + ';">' + generatedUser[0] + '</h6></li></ul></p><br></br></div><br>';


            })

            document.getElementsByTagName("A").onclick = function () {
            location.href = "{{ url_for('catalogue') }}";}


        }
    };
    xmlhttp.open("GET", url, true);
    xmlhttp.send();
}
