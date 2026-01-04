# -*- coding: utf-8 -*-
import json

# -------------------------------------------------------------------------
# Dados das 4 viaturas (mantidos iguais)
# -------------------------------------------------------------------------
viaturas = [
    {
        "nome_arquivo": "patrulha_vtr_01.html",
        "titulo": "VTR-01 - Pontos Fixos CPP 1.1 - SP",
        "pontos": [
            {"id": "PE 1",  "nome": "PE 1",  "endereco": "Av. José César de Oliveira, 21 - Vila Leopoldina",        "lat": -23.539600294412644, "lng": -46.73399579004857},
            {"id": "OP BLOQUEIO", "nome": "OP BLOQUEIO", "endereco": "Av. Dr. Gastão Vidigal, 1142 - Vila Leopoldina", "lat": -23.528903888196563, "lng": -46.739219300274584},
            {"id": "PE 2",  "nome": "PE 2",  "endereco": "Av. Queiroz Filho, 1700 - Vila Hamburguesa",             "lat": -23.543194691386972, "lng": -46.73265171533143},
            {"id": "PE 3",  "nome": "PE 3",  "endereco": "Av. Queiroz Filho, 1315 - Portão 2 - Parque Villa-Lobos", "lat": -23.54182339721191,  "lng": -46.73028311175224},
            {"id": "PE 4",  "nome": "PE 4",  "endereco": "Av. Queiroz Filho, 113 - Parque da Lapa",                 "lat": -23.537408346784343, "lng": -46.721304176823345},
        ]
    },
    {
        "nome_arquivo": "patrulha_vtr_02.html",
        "titulo": "VTR-02 - Pontos Fixos CPP 1.2 - SP",
        "pontos": [
            {"id": "PE 1",  "nome": "PE 1",  "endereco": "Av. Queiroz Filho, 1310 - Vila Leopoldina",              "lat": -23.541005329058063, "lng": -46.730221538416615},
            {"id": "OP BLOQUEIO", "nome": "OP BLOQUEIO", "endereco": "Av. Dr. Gastão Vidigal, 1142 - Vila Leopoldina", "lat": -23.528903888196563, "lng": -46.739219300274584},
            {"id": "PE 2",  "nome": "PE 2",  "endereco": "Av. Mofarrej, 471 - Vila Leopoldina",                    "lat": -23.52719092456514,  "lng": -46.74024023237906},
            {"id": "PE 3",  "nome": "PE 3",  "endereco": "Av. Dr. Gastão Vidigal, 1399 - Vila Leopoldina",         "lat": -23.530055448171137, "lng": -46.73768108820495},
            {"id": "PE 4",  "nome": "PE 4",  "endereco": "Av. Dr. Gastão Vidigal, 2026 - Vila Leopoldina",         "lat": -23.53536877006379,  "lng": -46.733409818883544},
        ]
    },
    {
        "nome_arquivo": "patrulha_vtr_03.html",
        "titulo": "VTR-03 - Pontos Fixos CPP 2 - SP",
        "pontos": [
            {"id": "PE 1", "nome": "PE 1", "endereco": "R. Guaipá, 1028 - Lapa",                             "lat": -23.521029268046917, "lng": -46.732261188204845},
            {"id": "PE 2", "nome": "PE 2", "endereco": "Praça Ada Rogato - Alto da Lapa",                    "lat": -23.525864791078664, "lng": -46.728401953331854},
            {"id": "PE 3", "nome": "PE 3", "endereco": "Praça Augusto Ruschi - Alto da Lapa",                "lat": -23.52784041084019,  "lng": -46.72500045333086},
            {"id": "PE 4", "nome": "PE 4", "endereco": "R. Carlos Weber, 1700 - Vila Leopoldina",            "lat": -23.53387488628212,  "lng": -46.724876990048614},
            {"id": "PE 5", "nome": "PE 5", "endereco": "R. Schilling, 390 - Vila Leopoldina",                "lat": -23.530082527805497, "lng": -46.728577961213965},
        ]
    },
    {
        "nome_arquivo": "patrulha_vtr_04.html",
        "titulo": "VTR-04 - Pontos Fixos CPP 3 - SP",
        "pontos": [
            {"id": "PE 1", "nome": "PE 1", "endereco": "Praça Senador José Roberto Leite Penteado, 1083 - Lapa", "lat": -23.521395755450254, "lng": -46.71906784587471},
            {"id": "PE 2", "nome": "PE 2", "endereco": "R. Monte Pascal, 210 - Lapa",                               "lat": -23.519726953698694, "lng": -46.722041978984215},
            {"id": "PE 3", "nome": "PE 3", "endereco": "Av. Raimundo Pereira de Magalhães, 200 - Jardim Iris",     "lat": -23.518211052120805, "lng": -46.71211297470965},
            {"id": "PE 4", "nome": "PE 4", "endereco": "Praça Senador José Roberto Leite Penteado, 1083 - Lapa",    "lat": -23.521395755450254, "lng": -46.71906784587471},
            {"id": "PE 5", "nome": "PE 5", "endereco": "Rua Monte Pascal, 247 - Lapa",                              "lat": -23.519381740760938, "lng": -46.723333961214365},
            {"id": "PE 6", "nome": "PE 6", "endereco": "Praça Anibal de Marcondes Amaral - Lapa",                   "lat": -23.52263172665733,  "lng": -46.71798155333337},
        ]
    }
]

# -------------------------------------------------------------------------
# TODOS OS TRÊS POLÍGONOS CPP (copiados exatamente do seu HTML original)
# -------------------------------------------------------------------------
cpp_geojson = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": { "name": "CPP-01", "fillColor": "#FBC02D" },
            "geometry": {
                "type": "Polygon",
                "coordinates": [[
                    [-46.7412559, -23.5180041], [-46.7431222, -23.5181629], [-46.7445164, -23.5185972],
                    [-46.7454387, -23.5193068], [-46.7464038, -23.5206067], [-46.747167, -23.5219729],
                    [-46.7478443, -23.5236145], [-46.7479638, -23.5253348], [-46.7480832, -23.5274879],
                    [-46.7478501, -23.5314007], [-46.747476, -23.5330029], [-46.7465011, -23.5342904],
                    [-46.740155, -23.5399125], [-46.7341064, -23.5452414], [-46.7336367, -23.5449049],
                    [-46.7255717, -23.5374365], [-46.726738, -23.5356636], [-46.7281617, -23.5340482],
                    [-46.7311806, -23.5308959], [-46.7369607, -23.5245126], [-46.7402437, -23.5272473],
                    [-46.7410413, -23.5256378], [-46.7411701, -23.5228047], [-46.7412559, -23.5180041]
                ]]
            }
        },
        {
            "type": "Feature",
            "properties": { "name": "CPP-02", "fillColor": "#7CB342" },
            "geometry": {
                "type": "Polygon",
                "coordinates": [[
                    [-46.7412559, -23.5180041], [-46.7411701, -23.5228047], [-46.7410413, -23.5256378],
                    [-46.7402437, -23.5272473], [-46.7369607, -23.5244339], [-46.7311806, -23.5308959],
                    [-46.726738, -23.5356636], [-46.7255717, -23.5373578], [-46.7248435, -23.5371399],
                    [-46.7240509, -23.5370205], [-46.7224013, -23.5372143], [-46.7210307, -23.537408],
                    [-46.7204205, -23.5373672], [-46.7199116, -23.5371796], [-46.7194962, -23.536771],
                    [-46.7191237, -23.5362444], [-46.7186034, -23.5359382], [-46.7183191, -23.5346286],
                    [-46.7194028, -23.5314391], [-46.7204543, -23.5269485], [-46.7213556, -23.5248925],
                    [-46.7222568, -23.5213807], [-46.7235227, -23.5196445], [-46.7248423, -23.51856],
                    [-46.7257596, -23.5174274], [-46.726076, -23.5152718], [-46.730976, -23.5178438],
                    [-46.7329578, -23.5183302], [-46.7412559, -23.5180041]
                ]]
            }
        },
        {
            "type": "Feature",
            "properties": { "name": "CPP-03", "fillColor": "#01579B" },
            "geometry": {
                "type": "Polygon",
                "coordinates": [[
                    [-46.726076, -23.5152718], [-46.7257596, -23.5174274], [-46.7248423, -23.51856],
                    [-46.7235227, -23.5196445], [-46.7222568, -23.5213807], [-46.7213556, -23.5248925],
                    [-46.7204543, -23.5269485], [-46.7195369, -23.5308672], [-46.7183191, -23.5346286],
                    [-46.7186034, -23.5359382], [-46.7191237, -23.5362444], [-46.7143493, -23.5353639],
                    [-46.7130918, -23.5323588], [-46.7128724, -23.5306299], [-46.7132455, -23.5268636],
                    [-46.7135608, -23.5239771], [-46.7134899, -23.5232744], [-46.7130452, -23.5228146],
                    [-46.7125654, -23.5223486], [-46.7122933, -23.5218598], [-46.712168, -23.52134],
                    [-46.7121268, -23.5207948], [-46.7120847, -23.5206107], [-46.7115062, -23.520407],
                    [-46.713534, -23.5141993], [-46.7144727, -23.5111348], [-46.7140623, -23.5105962],
                    [-46.7141529, -23.5099057], [-46.7143936, -23.5093726], [-46.7142313, -23.5090541],
                    [-46.7171172, -23.5088968], [-46.7186327, -23.5089312], [-46.7193368, -23.5091747],
                    [-46.7198906, -23.5095559], [-46.7206698, -23.5102963], [-46.722715, -23.5130829],
                    [-46.726076, -23.5152718]
                ]]
            }
        }
    ]
}

# -------------------------------------------------------------------------
# Template HTML (atualizado com legenda completa dos 3 CPPs)
# -------------------------------------------------------------------------
html_template = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>{titulo}</title>

    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/leaflet@1.9.4/dist/leaflet.css" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css" />
    <script src="https://cdn.jsdelivr.net/npm/leaflet@1.9.4/dist/leaflet.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.min.js"></script>

    <style>
        body {{ margin:0; padding:0; font-family:Arial, sans-serif; background:#000; color:#fff; min-height:100vh; display:flex; flex-direction:column; }}
        header {{ background:#1a1a1a; padding:20px; text-align:center; }}
        h1 {{ margin:0; font-size:2.1rem; }}
        .back-btn {{ display:inline-block; margin:15px 20px; padding:12px 24px; background:#333; color:white; border-radius:8px; text-decoration:none; font-weight:bold; }}
        .back-btn:hover {{ background:#555; }}
        .folium-map {{ width:100%; height:calc(100vh - 300px); border-radius:12px; overflow:hidden; box-shadow:0 6px 15px rgba(0,0,0,0.8); }}
        footer {{ text-align:center; padding:12px; background:#1a1a1a; font-size:0.8rem; color:#888; }}
        .popup-link {{ color: #ff4d4d; font-weight: bold; text-decoration: underline; }}
        .control-panel {{ background:#1a1a1a; padding:16px; text-align:center; }}
        .point-btn {{ margin:6px 4px; padding:12px 20px; background:#333; color:white; border:none; border-radius:8px; cursor:pointer; font-weight:bold; transition: all 0.2s; min-width:120px; }}
        .point-btn:hover {{ background:#555; }}
        .point-btn.active {{ background:#0066cc; }}
        .legend {{ margin:12px auto; max-width:700px; font-size:0.95rem; color:#ccc; text-align:center; }}
        .legend span {{ margin:0 16px; }}
        .legend .cpp01 {{ color:#FBC02D; }}
        .legend .cpp02 {{ color:#7CB342; }}
        .legend .cpp03 {{ color:#01579B; }}
    </style>
</head>
<body>

    <header><h1>{titulo}</h1></header>

    <a href="index.html" class="back-btn">← Voltar ao Menu Principal</a>

    <div class="control-panel">
        {botoes_html}
        <div class="legend">
            <span class="cpp01">██ CPP-01</span>
            <span class="cpp02">██ CPP-02</span>
            <span class="cpp03">██ CPP-03</span>
        </div>
    </div>

    <div class="folium-map" id="mapa"></div>

    <footer>Sistema de Informação OBE • {vtr_nome} • 2025</footer>

    <script>
        var map = L.map('mapa', {{
            center: [-23.53, -46.73],
            zoom: 14,
            zoomControl: true
        }});

        L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
            attribution: '© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
            maxZoom: 19
        }}).addTo(map);

        // Polígonos CPP (todos os três sempre visíveis)
        const cppData = {cpp_geojson_json};

        L.geoJSON(cppData, {{
            style: feature => ({{
                color: feature.properties.fillColor,
                weight: 2.5,
                opacity: 0.9,
                fillColor: feature.properties.fillColor,
                fillOpacity: 0.25
            }}),
            onEachFeature: (feature, layer) => {{
                layer.bindPopup(`<b>Área ${{feature.properties.name}}</b>`);
            }}
        }}).addTo(map);

        // Marcadores
        const marcadores = {{}};
        const icons = {{
            'OP BLOQUEIO': L.AwesomeMarkers.icon({{icon: 'ban', markerColor: 'red', prefix: 'fa', iconColor: 'white'}}),
            'default':      L.AwesomeMarkers.icon({{icon: 'car', markerColor: 'blue', prefix: 'fa', iconColor: 'white'}})
        }};

        const pontos = {pontos_json};

        pontos.forEach(p => {{
            const icone = (p.id.includes('BLOQUEIO')) ? icons['OP BLOQUEIO'] : icons['default'];
            const marker = L.marker([p.lat, p.lng], {{icon: icone}}).addTo(map)
                .bindPopup(`
                    <b>${{p.nome}}</b><br>
                    ${{p.endereco}}<br><br>
                    <a href="https://www.google.com/maps/search/?api=1&query=${{p.lat}},${{p.lng}}" target="_blank" class="popup-link">
                        Abrir no Google Maps →
                    </a>
                `);
            marcadores[p.id] = marker;
        }});

        // Função dos botões
        function centralizar(id) {{
            document.querySelectorAll('.point-btn').forEach(b => b.classList.remove('active'));
            const btn = document.querySelector(`.point-btn[data-id="${{id}}"]`);
            if (btn) btn.classList.add('active');

            const m = marcadores[id];
            if (m) {{
                map.setView(m.getLatLng(), 16, {{ animate: true }});
                m.openPopup();
            }}
        }}

        // Inicializa abrindo o primeiro ponto
        if (Object.keys(marcadores).length > 0) {{
            centralizar(Object.keys(marcadores)[0]);
        }}
        setTimeout(() => map.invalidateSize(), 300);
        window.addEventListener('resize', () => setTimeout(() => map.invalidateSize(), 200));
    </script>
</body>
</html>
"""

# -------------------------------------------------------------------------
# Geração dos 4 arquivos HTML
# -------------------------------------------------------------------------
for vtr in viaturas:
    botoes = []
    for p in vtr["pontos"]:
        botoes.append(
            f'<button class="point-btn" data-id="{p["id"]}" onclick="centralizar(\'{p["id"]}\')">{p["id"]}</button>'
        )

    conteudo = html_template.format(
        titulo          = vtr["titulo"],
        vtr_nome        = vtr["nome_arquivo"].split('.')[0].upper().replace('_', '-'),
        botoes_html     = "\n        ".join(botoes),
        cpp_geojson_json = json.dumps(cpp_geojson, ensure_ascii=False),
        pontos_json     = json.dumps(vtr["pontos"], ensure_ascii=False)
    )

    with open(vtr["nome_arquivo"], "w", encoding="utf-8") as f:
        f.write(conteudo)

    print(f"Gerado: {vtr['nome_arquivo']}  ({len(vtr['pontos'])} pontos)")