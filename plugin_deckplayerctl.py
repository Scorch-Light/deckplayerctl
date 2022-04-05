import subprocess

class Plugin:
    # The name of the plugin. This string will be displayed in the Plugin menu
    name = "DeckPlayerControl"
    # The name of the plugin author
    author = "ScorchLight"

    # If the plugin should be reloaded from a call to /plugins/reload or a file change
    hot_reload = True

    # The HTML that will be loaded when selecting the plugin in the list
    main_view_html = """<html><head></head><body>
    	

		    <div style="width:100%; text-align: center;">
		        <button id="playerctl_btn_prev" style="display:inline-block; border-radius: 100px; background: #23262e; color: #dcdedf;">
		            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-caret-left-fill" viewBox="0 0 16 16">
		                <path d="m3.86 8.753 5.482 4.796c.646.566 1.658.106 1.658-.753V3.204a1 1 0 0 0-1.659-.753l-5.48 4.796a1 1 0 0 0 0 1.506z"/>
		            </svg>
		        </button>
		        <button id="playerctl_btn_play"  style="display:inline-block; border-radius: 100px; background: #23262e; color: #dcdedf;">
		            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-play-fill" viewBox="0 0 16 16">
		                <path d="m11.596 8.697-6.363 3.692c-.54.313-1.233-.066-1.233-.697V4.308c0-.63.692-1.01 1.233-.696l6.363 3.692a.802.802 0 0 1 0 1.393z"/>
		            </svg>
		        </button>
		        <button id="playerctl_btn_next"  style="display:inline-block; border-radius: 100px; background: #23262e; color: #dcdedf;">
		            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-caret-right-fill" viewBox="0 0 16 16">
		                <path d="m12.14 8.753-5.482 4.796c-.646.566-1.658.106-1.658-.753V3.204a1 1 0 0 1 1.659-.753l5.48 4.796a1 1 0 0 1 0 1.506z"/>
		            </svg>
		        </button>
		    </div>
		<script>
		    const MUSIC_ICON_SVG = `
		        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-music-note" viewBox="0 0 16 16">
		            <path d="M9 13c0 1.105-1.12 2-2.5 2S4 14.105 4 13s1.12-2 2.5-2 2.5.895 2.5 2z"/>
		            <path fill-rule="evenodd" d="M9 3v10H8V3h1z"/>
		            <path d="M8 2.82a1 1 0 0 1 .804-.98l3-.6A1 1 0 0 1 13 2.22V4L8 5V2.82z"/>
		        </svg>
		    `;
		    const PLAY_ICON = `
		    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-play-fill" viewBox="0 0 16 16">
		        <path d="m11.596 8.697-6.363 3.692c-.54.313-1.233-.066-1.233-.697V4.308c0-.63.692-1.01 1.233-.696l6.363 3.692a.802.802 0 0 1 0 1.393z"/>
		    </svg>
		    `
		    const PAUSE_ICON = `
		    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pause-fill" viewBox="0 0 16 16">
		        <path d="M5.5 3.5A1.5 1.5 0 0 1 7 5v6a1.5 1.5 0 0 1-3 0V5a1.5 1.5 0 0 1 1.5-1.5zm5 0A1.5 1.5 0 0 1 12 5v6a1.5 1.5 0 0 1-3 0V5a1.5 1.5 0 0 1 1.5-1.5z"/>
		    </svg>
		    `

		     document.getElementById("playerctl_btn_prev").onclick = function(event){
		        call_plugin_method("ctlprev", {});
		        event.stopPropagation();
		        
		    };
		     document.getElementById("playerctl_btn_play").onclick = function(event){
		        call_plugin_method("ctlplay"), {};
		        event.stopPropagation();
		    };
		     document.getElementById("playerctl_btn_next").onclick = function(event){		   
		        call_plugin_method("ctlnext", {});
		          event.stopPropagation(); 
		        
		    };
		</script></body></html>"""

    # The HTML that will be used to display a widget in the plugin main page
    tile_view_html = """
		<div class="quickaccesscontrols_PanelSectionRow_26R5w" style="background: #23262e; border-radius: 5px;">
		    <div style="display: inline-block;">
		        <div id="current_artist">Nothing playing</div>
		        <div id="current_song"></div>
		    </div>
		    <div style="width:100%; text-align: center;">
		        <button id="playerctl_btn_prev" style="display:inline-block; border-radius: 100px; background: #23262e; color: #dcdedf;">
		            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-caret-left-fill" viewBox="0 0 16 16">
		                <path d="m3.86 8.753 5.482 4.796c.646.566 1.658.106 1.658-.753V3.204a1 1 0 0 0-1.659-.753l-5.48 4.796a1 1 0 0 0 0 1.506z"/>
		            </svg>
		        </button>
		        <button id="playerctl_btn_play"  style="display:inline-block; border-radius: 100px; background: #23262e; color: #dcdedf;">
		            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-play-fill" viewBox="0 0 16 16">
		                <path d="m11.596 8.697-6.363 3.692c-.54.313-1.233-.066-1.233-.697V4.308c0-.63.692-1.01 1.233-.696l6.363 3.692a.802.802 0 0 1 0 1.393z"/>
		            </svg>
		        </button>
		        <button id="playerctl_btn_next" style="display:inline-block; border-radius: 100px; background: #23262e; color: #dcdedf;">
		            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-caret-right-fill" viewBox="0 0 16 16">
		                <path d="m12.14 8.753-5.482 4.796c-.646.566-1.658.106-1.658-.753V3.204a1 1 0 0 1 1.659-.753l5.48 4.796a1 1 0 0 1 0 1.506z"/>
		            </svg>
		        </button>
		    </div>
		</div>
		<script>
		    const MUSIC_ICON_SVG = `
		        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-music-note" viewBox="0 0 16 16">
		            <path d="M9 13c0 1.105-1.12 2-2.5 2S4 14.105 4 13s1.12-2 2.5-2 2.5.895 2.5 2z"/>
		            <path fill-rule="evenodd" d="M9 3v10H8V3h1z"/>
		            <path d="M8 2.82a1 1 0 0 1 .804-.98l3-.6A1 1 0 0 1 13 2.22V4L8 5V2.82z"/>
		        </svg>
		    `;
		    const PLAY_ICON = `
		    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-play-fill" viewBox="0 0 16 16">
		        <path d="m11.596 8.697-6.363 3.692c-.54.313-1.233-.066-1.233-.697V4.308c0-.63.692-1.01 1.233-.696l6.363 3.692a.802.802 0 0 1 0 1.393z"/>
		    </svg>
		    `
		    const PAUSE_ICON = `
		    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pause-fill" viewBox="0 0 16 16">
		        <path d="M5.5 3.5A1.5 1.5 0 0 1 7 5v6a1.5 1.5 0 0 1-3 0V5a1.5 1.5 0 0 1 1.5-1.5zm5 0A1.5 1.5 0 0 1 12 5v6a1.5 1.5 0 0 1-3 0V5a1.5 1.5 0 0 1 1.5-1.5z"/>
		    </svg>
		    `

		     document.getElementById("playerctl_btn_prev").onclick = function(event){
		        call_plugin_method("ctlprev", {});
		        event.stopPropagation();
		        
		    };
		     document.getElementById("playerctl_btn_play").onclick = function(event){
		        call_plugin_method("ctlplay"), {};
		        event.stopPropagation();
		    };
		     document.getElementById("playerctl_btn_next").onclick = function(event){		   
		     	call_plugin_method("ctlnext", {});
		        event.stopPropagation(); 
		        
		    };
		</script>
    """

    # A normal method. It can be called from JavaScript using call_plugin_function("method_1", argument1, argument2)
               
    async def ctlnext(self):
        subprocess.Popen("playerctl next", stdout=subprocess.PIPE, shell=True).communicate()
     
    async def ctlplay(self):
        subprocess.Popen("playerctl play-pause", stdout=subprocess.PIPE, shell=True).communicate()
  
         
    async def ctlprev(self):
        subprocess.Popen("playerctl previous", stdout=subprocess.PIPE, shell=True).communicate()

