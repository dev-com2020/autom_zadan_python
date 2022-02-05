(function() {
	var Realmac = Realmac || {};

	Realmac.meta = {
		
		// Ustawianie nagłówka w przeglądarce.
		//
		// @var String text
		setTitle: function(text) {
			return document.title = text;
		},
		
		// Ustawianie atrybutów metaznaczników.
		//
		// @var String name
		// @var String content
		setTagContent: function(tag, content){
			// Jeśli ustawiany znacznik to title, 
			// zwracany jest wynik wywołania setTitle.
			if ( tag === 'title' )
			{
				return this.setTitle(content);
			}
			
			// W przeciwnym razie kod próbuje znaleźć dany metaznacznik.
			var tag = this.getTag(tag);
			
			// Jeśli znaleziono znacznik, należy ustawić jego wartość.
			if ( tag !== false )
			{
				return tag.setAttribute('content', content);
			}
			
			return false;
		},
		
		// Znajduje metaznacznik
		//
		// @var String name
		getTag: function(name) {
			var meta = document.querySelectorAll('meta');
			
			for ( var i=0; i<meta.length; i++ )
			{
				if (meta[i].name == name){
					return meta[i];
				}
			}
			
			var tag = document.createElement('meta');
			tag.name = name;
			document.getElementsByTagName('head')[0].appendChild(tag);
			
			return tag;
		}
	};
 
	// Obiekt zawierający wszystkie metainformacje z witryny.
	var websiteMeta = {"5eabef23f63024c20389c34b94dee593-1.html":"Krótszy artykuł z informacjami o Pythonie\n\nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut ","archive-september-2018.html":"Archiwa z września 2018","33714fc865e02aeda2dabb9a42a787b2-0.html":"Artykuł z dużą ilością tekstu\n\nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore m","b93bec5d9681df87e6e8d5703ed7cd81-2.html":"\nLorem ipsum dolor sit amet, harum invenire persequeris sea te. Ne partem causae his, te partiendo consequuntur per. Case vero option mea te, mea opor"};
 
	// pageId musi pasować do klucza z obiektu websiteMeta.
	var url = window.location.pathname;
	var pageId = url.substring(url.lastIndexOf('/')+1);
	if (!pageId || pageId.length == 0){
		pageId = 'index.html';
	}
	pageMeta = websiteMeta[pageId];
 
	// Wykonywane, jeśli dostępne są metainformacje dla danej strony.
	if (pageMeta){
		Realmac.meta.setTagContent('description', pageMeta);
	}
 
 })();