# -*- coding: utf-8 -*-
"""Base de dados do estudo de concorrência Quaddra Sabiá (produtos 200 m²+).
Gera data.json (para o HTML) e sheets.json (para o Google Sheets)."""
import json, math, urllib.parse

DATA_CHECAGEM = "03/11/2026"

# Posições: metros a partir do Quaddra (x = leste, y = norte).
# "mapa" = medido sobre os mapas dos estudos Yuny fev/26 e jul/26 (±100 m)
# "estimada" = estimada pelo endereço sobre o mapa de 1 km do estudo jul/26 (±300-400 m)

P = []  # projetos
def proj(**k):
    k.setdefault("pos_base", "mapa")
    P.append(k)

QUADDRA = dict(
    id="Q", nome="Quaddra Sabiá", incorporadora="Yuny",
    endereco="Av. Sabiá (frente ao Lindenberg Moema) - nº a confirmar",
    anel="Projeto base", segmento="", status_obra="Pré-lançamento (SCP)",
    lancamento="", entrega="", torres="1", pavimentos="", unidades="", unid_andar="2",
    terreno="", metragens="~298, ~350, ~395 (9 unid.)", suites="", vagas="",
    arquitetura="", paisagismo="", interiores="", vgv="",
    estudos_yuny="Base", status_dado="Base interna (Rogerio)",
    obs="Elevadores privativos; tênis oficial de saibro; piscina coberta raia 25 m + descoberta com solarium; Technogym; loja GPA no térreo com acesso independente.",
    fonte1="Base enviada pelo Rogerio em 03/11/2026", fonte2="",
    x=0, y=0, pos_base="mapa",
)

# ---------------- ANEL 1 (até 1 km) ----------------
proj(id="C01", nome="Lindenberg Moema", alias="Lindenberg Inhambu (estudo fev/26)", incorporadora="Adolpho Lindenberg",
     endereco="Av. Juriti x R. Inhambu, Moema", anel="Anel 1", status_obra="Lançamento",
     lancamento="11/2025", entrega="11/2028", torres="1", pavimentos="", unidades="58 (fev/26: 29+29)", unid_andar="?",
     terreno="3400", metragens="293 / 373", suites="4", vagas="4", arquitetura="", paisagismo="", interiores="", vgv="",
     estudos_yuny="Fev/26 e Jul/26", status_dado="Confirmado (2 fontes)",
     obs="Em frente ao Quaddra. Fev/26 lista 291 m² com 3 suítes; portais dizem 293 m² com 4 suítes. Lazer com quadra de tênis e piscina coberta (Apto).",
     fonte1="https://apto.vc/br/sp/sao-paulo/moema/lindenberg-moema", fonte2="https://myside.com.br/apartamento-venda-lindenberg-moema-sao-paulo-sp",
     x=58, y=101)
proj(id="C02", nome="La Galerie", alias="Cyrela Gaivota (fev/26); provável = 'Breve lançamento R. Lavandisca' (Apto)", incorporadora="Cyrela + Nortis",
     endereco="R. Gaivota, 418, Moema", anel="Anel 1", status_obra="Lançamento",
     lancamento="06/2026", entrega="02/2030 (MySide) ou 12/2031 (Apto)", torres="1 ou 2 (divergente)", pavimentos="", unidades="", unid_andar="1 na planta de 416 m²",
     terreno="4420", metragens="284 / 345 / 416 / 442 / 570 / 649 / 770 (duplex e casas suspensas)", suites="4", vagas="3 a 5",
     arquitetura="", paisagismo="", interiores="", vgv="",
     estudos_yuny="Fev/26 e Jul/26 (incompleto)", status_dado="Divergente",
     obs="Estudos Yuny só trazem 283/288, 345 e 416 m². Lazer: piscina com raia, piscina coberta, quadra de tênis, spa. Loft descreve 2 torres (uma 1/andar); Apto diz 1 torre. Apto lista à parte um 'Breve lançamento R. Lavandisca' 283-415 m² com tênis: provável duplicidade.",
     fonte1="https://myside.com.br/apartamento-venda-la-galerie-sao-paulo-sp", fonte2="https://apto.vc/br/sp/sao-paulo/moema/la-galerie-moema",
     x=203, y=-34)
proj(id="C03", nome="Casa Sabiá", alias="", incorporadora="Even",
     endereco="Av. Sabiá, 598 (quadra Sabiá / Arapanés / Jauaperi)", anel="Anel 1", status_obra="Em obra",
     lancamento="12/2023 (Apto: 02/2024)", entrega="08/2027", torres="2 residenciais + subcondomínio de studios", pavimentos="T+24", unidades="74 (fev/26: 70)", unid_andar="",
     terreno="5570", metragens="311 / 315 / 317 / até 621", suites="3 a 4", vagas="4 a 5",
     arquitetura="", paisagismo="", interiores="", vgv="",
     estudos_yuny="Fev/26 e Jul/26", status_dado="Divergente",
     obs="Metragem diverge entre fontes (311, 315, 317). Laudo Kinea: empreendimento misto com subcondomínios independentes, incluindo torre de studios (Studio Sabiá) no mesmo terreno. Estará pronto antes do lançamento do Quaddra.",
     fonte1="https://apto.vc/br/sp/sao-paulo/moema/casa-sabia", fonte2="https://kinea.com.br/wp-content/uploads/2024/11/DoKRES_Outras-Informacoes_11-2024.pdf",
     x=237, y=-193)
proj(id="C04", nome="Singular Ibirapuera", alias="", incorporadora="Varicred",
     endereco="Av. Juriti, 129, Moema", anel="Anel 1", status_obra="Em obra",
     lancamento="07/2025 (fev/26: 02/2025)", entrega="07/2028", torres="1", pavimentos="", unidades="28", unid_andar="1",
     terreno="1600", metragens="317", suites="4", vagas="4",
     arquitetura="Jonas Birger", paisagismo="Rodrigo Oliveira", interiores="Gui Mattos (áreas comuns)", vgv="",
     estudos_yuny="Fev/26 e Jul/26", status_dado="Confirmado (2 fontes)",
     obs="1 apartamento por andar, elevador delivery exclusivo por unidade, piscina coberta. Data de lançamento diverge entre os estudos Yuny.",
     fonte1="https://myside.com.br/apartamento-venda-singular-ibirapuera-sao-paulo-sp", fonte2="https://apto.vc/br/sp/sao-paulo/ibirapuera/singular-ibirapuera",
     x=116, y=130)
proj(id="C05", nome="Splend Moema", alias="", incorporadora="Exto",
     endereco="Av. Juriti, 646, Moema", anel="Anel 1", status_obra="Em obra",
     lancamento="09/2024 (Apto: 02/2025)", entrega="10/2027", torres="1", pavimentos="", unidades="48 (fev/26: 26+22)", unid_andar="",
     terreno="1835", metragens="258", suites="4", vagas="3 ou 4",
     arquitetura="Exto (Dina Melaragno)", paisagismo="", interiores="", vgv="",
     estudos_yuny="Fev/26 e Jul/26", status_dado="Confirmado (2 fontes)",
     obs="Abaixo das nossas metragens. Piscina de 20 m, quadra de tênis Lisonda (piso sintético), Life Fitness, hall privativo, depósito.",
     fonte1="https://myside.com.br/apartamento-venda-splend-moema-sao-paulo-sp", fonte2="https://apto.vc/br/sp/sao-paulo/moema/splend-moema",
     x=411, y=-208)
proj(id="C06", nome="Agami Park Residences", alias="", incorporadora="EZTEC",
     endereco="Av. Agami, 220, Moema", anel="Anel 1", status_obra="Em obra",
     lancamento="02/2025", entrega="01/2029", torres="1", pavimentos="25", unidades="45 + 1 loja", unid_andar="2",
     terreno="1554", metragens="215 / 290 / 381 / 424 / 572 (garden, tipo, duplex)", suites="3 a 4", vagas="3 a 4",
     arquitetura="", paisagismo="", interiores="", vgv="R$ 318 mi",
     estudos_yuny="Fev/26 e Jul/26 (incompleto)", status_dado="Confirmado (RI EZTEC + portal)",
     obs="Estudos Yuny só trazem 215 e 290 m²; as plantas de 381/424/572 m² competem com as nossas de 350 e 395. Piscina semiolímpica (25 m), 6 elevadores. Tem 1 loja.",
     fonte1="https://myside.com.br/apartamento-venda-agami-park-residences-sao-paulo-sp", fonte2="https://visnoinvest.com.br/news/6266/eztec-lanca-empreendimento-de-alto-padrao-por-r-318-milhoes",
     x=483, y=10)
proj(id="C07", nome="Vista Parque Ibirapuera", alias="", incorporadora="Kallas",
     endereco="Av. República do Líbano, 2112", anel="Anel 1", status_obra="Em obra",
     lancamento="11/2025 (jul/26: 06/2025)", entrega="06/2028 a 08/2028", torres="1", pavimentos="29 a 30", unidades="38 a 40", unid_andar="2",
     terreno="2530", metragens="373 / 453 / 1.185 (cobertura)", suites="4 a 5", vagas="5 a 10",
     arquitetura="PSA Arquitetura", paisagismo="Benedito Abbud", interiores="Triptyque", vgv="",
     estudos_yuny="Fev/26 e Jul/26", status_dado="Confirmado (2 fontes)",
     obs="Vista para o Parque Ibirapuera. Piscina coberta, quadra de tênis, gerador full. Data de lançamento diverge entre os estudos Yuny.",
     fonte1="https://myside.com.br/apartamento-venda-vista-parque-ibirapuera-sao-paulo-sp", fonte2="https://apto.vc/br/sp/sao-paulo/ibirapuera/vista-parque-ibirapuera",
     x=464, y=145)
proj(id="C08", nome="Edifício Adolpho Lindenberg", alias="Lindenberg Canário (estudo fev/26)", incorporadora="Adolpho Lindenberg",
     endereco="R. Canário, 133, Moema", anel="Anel 1", status_obra="Lançamento",
     lancamento="06/2026", entrega="02/2031", torres="1", pavimentos="", unidades="75", unid_andar="",
     terreno="", metragens="330 / 332 / 430 / 470", suites="4", vagas="4",
     arquitetura="", paisagismo="", interiores="", vgv="R$ 1,2 bi",
     estudos_yuny="Só fev/26 (sumiu em jul/26)", status_dado="Confirmado (2 fontes)",
     obs="Vendeu mais da metade das 75 unidades nos primeiros dias (imprensa). Não aparece no estudo de julho.",
     fonte1="https://myside.com.br/apartamento-venda-edificio-adolpho-lindenberg-sao-paulo-sp", fonte2="https://paraibabusiness.com.br/wellness-e-nome-proprio-a-formula-de-r-12-bi-da-lindenberg/",
     x=280, y=159)
proj(id="C09", nome="Almaz República do Líbano", alias="República do Líbano (fev/26); provável = 'Luxury Home' (Apto)", incorporadora="R. Yazbek (fev/26: Varicred, Luni e Yazbek)",
     endereco="Av. República do Líbano (nº a confirmar)", anel="Anel 1", status_obra="Breve lançamento",
     lancamento="10/2026", entrega="12/2031", torres="1", pavimentos="", unidades="42 a 44", unid_andar="",
     terreno="", metragens="335 / 336 / 431 / até 851", suites="3 a 4", vagas="3 a 8",
     arquitetura="", paisagismo="", interiores="", vgv="",
     estudos_yuny="Só fev/26", status_dado="Divergente",
     obs="Apto lista 'Almaz' (336/431) e 'Luxury Home' (335-851, R. Yazbek, 44 unid.) na mesma avenida e com mesma entrega: provável mesmo projeto.",
     fonte1="https://apto.vc/br/sp/sao-paulo/moema/almaz-republica-do-libano", fonte2="https://apto.vc/br/sp/sao-paulo/moema/luxury-home",
     x=585, y=39)
proj(id="C10", nome="Maison Gabrielle", alias="", incorporadora="Zabo Engenharia",
     endereco="Av. Pavão, 246, Moema", anel="Anel 1", status_obra="Lançamento",
     lancamento="04/2026", entrega="04/2029", torres="1", pavimentos="", unidades="", unid_andar="",
     terreno="", metragens="267 / 530", suites="4", vagas="3 e 4",
     arquitetura="", paisagismo="", interiores="", vgv="",
     estudos_yuny="Ausente", status_dado="Confirmado (2 fontes)",
     obs="Não aparece em nenhum estudo Yuny. Lazer listado: academia, piscina adulto, hidromassagem, brinquedoteca. Distância estimada pelo endereço.",
     fonte1="https://apto.vc/br/sp/sao-paulo/moema/maison-gabrielle", fonte2="https://www.lopes.com.br/lancamento/REM25673/maison-gabrielle-sao-paulo-indianopolis",
     x=-709, y=-154, pos_base="estimada")
proj(id="C11", nome="Aura Moema by Cyrela", alias="", incorporadora="Cyrela",
     endereco="Praça Nossa Senhora Aparecida, 58, Moema", anel="Anel 1", status_obra="Em obra (entrega 2026)",
     lancamento="10/2023", entrega="07/2026", torres="1", pavimentos="", unidades="46", unid_andar="",
     terreno="", metragens="250 / 251", suites="3 a 4", vagas="3 a 4",
     arquitetura="", paisagismo="", interiores="", vgv="",
     estudos_yuny="Ausente", status_dado="Confirmado (2 fontes)",
     obs="Concorrência parcial: planta única de 251 m², abaixo da nossa menor. Já pronto ou quase no lançamento do Quaddra. Distância estimada (junto à estação Moema).",
     fonte1="https://apto.vc/br/sp/sao-paulo/moema/aura-moema-by-cyrela", fonte2="https://www.quintoandar.com.br/condominio/aura-moema-moema-sao-paulo-p6js84v42k",
     x=480, y=-390, pos_base="estimada")
proj(id="C12", nome="LIS Moema", alias="", incorporadora="Cyrela",
     endereco="Al. dos Arapanés, 1335, Indianópolis", anel="Anel 1", status_obra="Em obra",
     lancamento="04/2023", entrega="11/2026", torres="3", pavimentos="", unidades="114", unid_andar="",
     terreno="6157", metragens="172 a 256", suites="2 a 4", vagas="2 a 3",
     arquitetura="", paisagismo="", interiores="", vgv="",
     estudos_yuny="Ausente", status_dado="1 fonte por dado",
     obs="Concorrência parcial (máximo 256 m²). Distância estimada, perto do limite de 1 km.",
     fonte1="https://apto.vc/br/sp/sao-paulo/moema/lis-moema", fonte2="https://myside.com.br/apartamento-venda-lis-moema-sao-paulo-sp",
     x=834, y=-357, pos_base="estimada")

# ---------------- ANEL 2 (1 a 2 km) ----------------
proj(id="C13", nome="Gran Oscar Ibirapuera", alias="Granoscar (Apto)", incorporadora="Trisul",
     endereco="Al. dos Anapurus, 410, Moema", anel="Anel 2", status_obra="Lançamento",
     lancamento="11/2025 a 01/2026", entrega="10/2029", torres="", pavimentos="", unidades="", unid_andar="",
     terreno="6289", metragens="353 / 370 / 395 / 412 / até 654 (fontes divergem)", suites="4", vagas="4",
     arquitetura="Perkins&Will", paisagismo="", interiores="", vgv="R$ 1,2 bi",
     estudos_yuny="Só jul/26", status_dado="Divergente",
     obs="Maior lançamento da história da Trisul. Condomínio estimado pela Trisul em R$ 6 a 7 mil/mês. Metragens divergem entre portais.",
     fonte1="https://myside.com.br/apartamento-venda-gran-oscar-ibirapuera-sao-paulo-sp", fonte2="https://www.moneytimes.com.br/trisul-tris3-lanca-seu-maior-projeto-com-apartamentos-de-ate-r-25-milhoes-igdl/",
     x=1063, y=-385)
proj(id="C14", nome="Monã The Grand Lodge", alias="", incorporadora="Diálogo Engenharia",
     endereco="Av. Indianópolis, 588", anel="Anel 2", status_obra="Em obra (entrega 2026)",
     lancamento="", entrega="10/2026", torres="", pavimentos="", unidades="", unid_andar="2",
     terreno="", metragens="177 / 197 / 247 / 290 / 332 / 356 / 380 / 572", suites="3 a 4", vagas="3 a 5",
     arquitetura="", paisagismo="", interiores="", vgv="",
     estudos_yuny="Ausente", status_dado="1 fonte por dado",
     obs="Não aparece nos estudos Yuny. 2 por andar, quadra de tênis e de beach tennis. Estará pronto quando o Quaddra lançar. Distância estimada pelo endereço.",
     fonte1="https://myside.com.br/apartamento-venda-mona-the-grand-lodge-sao-paulo-sp", fonte2="https://apto.vc/br/sp/sao-paulo/moema/mona-the-grand-lodge",
     x=1169, y=-287, pos_base="estimada")
proj(id="C15", nome="Nuv Moema", alias="", incorporadora="Planik",
     endereco="Av. Jamaris, 633, Moema", anel="Anel 2", status_obra="Lançamento",
     lancamento="", entrega="05/2029", torres="1", pavimentos="", unidades="", unid_andar="",
     terreno="1352", metragens="208 / 446 / 447", suites="3 a 4", vagas="3 a 4",
     arquitetura="", paisagismo="", interiores="", vgv="",
     estudos_yuny="Ausente", status_dado="Confirmado (2 fontes)",
     obs="Não aparece nos estudos Yuny. A planta de 446/447 m² concorre com a nossa de 395. Distância estimada pelo endereço.",
     fonte1="https://myside.com.br/apartamento-venda-nuv-moema-sao-paulo-sp", fonte2="https://apto.vc/br/sp/sao-paulo/moema/nuv-moema",
     x=963, y=-871, pos_base="estimada")
proj(id="C16", nome="Helbor Lens Moema", alias="", incorporadora="Helbor",
     endereco="Av. Indianópolis (nº a confirmar)", anel="Anel 2", status_obra="Breve lançamento",
     lancamento="", entrega="", torres="1", pavimentos="T+19", unidades="", unid_andar="",
     terreno="", metragens="157 a 476", suites="3", vagas="2 e 3",
     arquitetura="", paisagismo="", interiores="", vgv="",
     estudos_yuny="Ausente", status_dado="1 fonte por dado",
     obs="Concorrência parcial: só as plantas maiores (provavelmente coberturas) passam de 200 m². Posição muito incerta (número não divulgado).",
     fonte1="https://apto.vc/br/sp/sao-paulo/moema/helbor-lens-moema", fonte2="https://www.lopes.com.br/lancamento/REM25578/helbor-lens-moema-sao-paulo-moema",
     x=1349, y=-522, pos_base="estimada")
proj(id="C17", nome="Cyrela Zen by Yoo", alias="Zen Cyrela e Yoo (Apto)", incorporadora="Cyrela",
     endereco="R. Leopoldo de Bulhões, 40, Ibirapuera", anel="Anel 2", status_obra="Lançamento",
     lancamento="", entrega="12/2029", torres="2+", pavimentos="", unidades="", unid_andar="",
     terreno="", metragens="277 / 320 / 500", suites="3 a 4", vagas="3 a 4",
     arquitetura="", paisagismo="", interiores="Yoo", vgv="",
     estudos_yuny="Ausente", status_dado="Confirmado (2 fontes)",
     obs="Não aparece nos estudos Yuny. Hall privativo, elevador panorâmico na torre 1. A 700 m do metrô AACD-Servidor. Distância estimada.",
     fonte1="https://myside.com.br/apartamento-venda-cyrela-zen-by-yoo-sao-paulo-sp", fonte2="https://apto.vc/br/sp/sao-paulo/ibirapuera/zen-cyrela-e-yoo",
     x=1700, y=0, pos_base="estimada")
proj(id="C18", nome="Le Six Ibirapuera", alias="", incorporadora="Lavvi",
     endereco="Av. Chibarás, 133", anel="Anel 2", status_obra="Breve lançamento",
     lancamento="10/2026", entrega="09/2029", torres="1", pavimentos="", unidades="", unid_andar="",
     terreno="", metragens="194 / 264", suites="3 a 4", vagas="2 e 3",
     arquitetura="", paisagismo="", interiores="", vgv="",
     estudos_yuny="Ausente", status_dado="Confirmado (2 fontes)",
     obs="Concorrência parcial (máx. 264 m²). Proposta com serviços de hotelaria administrados pela CBRE; quadra de tênis. Distância estimada.",
     fonte1="https://myside.com.br/apartamento-venda-le-six-ibirapuera-sao-paulo-sp", fonte2="https://apto.vc/br/sp/sao-paulo/moema/le-six-ibirapuera",
     x=1300, y=-200, pos_base="estimada")
proj(id="C19", nome="Aiká Moema", alias="", incorporadora="CNL",
     endereco="Av. Chibarás, 669", anel="Anel 2", status_obra="Lançamento",
     lancamento="02/2026", entrega="08/2029", torres="1", pavimentos="", unidades="", unid_andar="",
     terreno="", metragens="124 a 259", suites="2 a 4", vagas="2 e 3",
     arquitetura="Jonas Birger e Carlos Rossi", paisagismo="", interiores="", vgv="",
     estudos_yuny="Ausente", status_dado="Confirmado (2 fontes)",
     obs="Concorrência parcial (só a planta de 259 m² passa de 200). Distância estimada.",
     fonte1="https://myside.com.br/apartamento-venda-aika-moema-sao-paulo-sp", fonte2="https://apto.vc/br/sp/sao-paulo/moema/aika-moema",
     x=1500, y=-600, pos_base="estimada")

# ---------------- REFERÊNCIA ----------------
REF = []
def ref(**k):
    k.setdefault("pos_base", "")
    REF.append(k)

ref(id="R01", nome="Arbórea Ibirapuera", segmento="Acima da faixa", incorporadora="Benx", endereco="Av. República do Líbano, 2000",
    status_obra="Breve lançamento", metragens="550 / 585 a 1.289", entrega="12/2031", distancia_aprox="≈ 530 m (mapa fev/26)",
    obs="Produto de outra faixa (a partir de 550-585 m²). Mesmo eixo do Vista Parque.", fonte1="https://apto.vc/br/sp/sao-paulo/ibirapuera/arborea-ibirapuera", fonte2="https://www.lopes.com.br/lancamento/REM25502/arborea-ibirapuera-sao-paulo-ibirapuera",
    x=522, y=87)
ref(id="R02", nome="Hélio 454", segmento="Pronto no lançamento / quase esgotado", incorporadora="RFM, Koema, RKG", endereco="Av. Hélio Pellegrino, 454, Vila Nova Conceição",
    status_obra="Entrega 11/2026", metragens="256 / 491", entrega="11/2026", distancia_aprox="≈ 350 m (mapa fev/26)",
    obs="8 unidades, 1 por andar. 85% vendido no estudo fev/26.", fonte1="https://myside.com.br/apartamento-venda-helio-454-sao-paulo-sp", fonte2="https://apto.vc/br/sp/sao-paulo/vila-nova-conceicao/helio-454",
    x=-266, y=222)
ref(id="R03", nome="Arbre Vila Nova", segmento="Esgotado (referência de preço)", incorporadora="", endereco="Vila Nova Conceição",
    status_obra="Entregue 12/2025", metragens="372", entrega="12/2025", distancia_aprox="≈ 300 m (mapa fev/26)",
    obs="100% vendido no estudo fev/26. Serve como referência de preço de lançamento (valor em atualização).", fonte1="Estudo Yuny fev/2026", fonte2="",
    x=19, y=304)
ref(id="R04", nome="Cyrela Moema by YOO", segmento="Pronto com estoque", incorporadora="Cyrela", endereco="Av. dos Imarés, 182",
    status_obra="Entregue 2024/2025", metragens="252 a 291", entrega="Entregue", distancia_aprox="≈ 1,2 a 1,6 km (estimada)",
    obs="Pronto para morar, junto ao Shopping Ibirapuera.", fonte1="https://myside.com.br/apartamento-venda-cyrela-moema-by-yoo-sao-paulo-sp", fonte2="https://apto.vc/br/sp/sao-paulo/moema/cyrela-moema-by-yoo", x=None, y=None)
ref(id="R05", nome="Saffire by Elie Saab", segmento="Pronto com estoque", incorporadora="Lavvi", endereco="Moema (endereço a confirmar)",
    status_obra="Pronto (Apto)", metragens="360 a 869", entrega="", distancia_aprox="a medir",
    obs="Primeiro residencial de grife (branded) da América do Sul, segundo a Lavvi.", fonte1="https://myside.com.br/venda-lancamentos-sao-paulo-sp/pagina-10", fonte2="https://www.2luxury2.com/saffire-residences-by-elie-saab-and-lavvi-south-americas-first-branded-haven", x=None, y=None)
ref(id="R06", nome="Park Lane Ibirapuera", segmento="Pronto com estoque", incorporadora="", endereco="a confirmar",
    status_obra="Pronto (Apto)", metragens="375 / 688", entrega="", distancia_aprox="a medir",
    obs="Listado como pronto no Apto (Moema). Estoque não confirmado.", fonte1="https://apto.vc/br/sp/sao-paulo/moema?page=7", fonte2="", x=None, y=None)
ref(id="R07", nome="Mirage Ibirapuera", segmento="Pronto com estoque", incorporadora="DZ Inc", endereco="a confirmar",
    status_obra="Pronto (Apto)", metragens="238 / 427", entrega="", distancia_aprox="a medir",
    obs="Listado como pronto no Apto. Estoque não confirmado.", fonte1="https://apto.vc/br/sp/sao-paulo/moema?page=7", fonte2="", x=None, y=None)
ref(id="R08", nome="Park Avenue", segmento="Pronto com estoque", incorporadora="EZTEC", endereco="a confirmar",
    status_obra="Pronto (Apto)", metragens="240 / 298", entrega="", distancia_aprox="a medir",
    obs="Listado como pronto no Apto. Estoque não confirmado.", fonte1="https://apto.vc/br/sp/sao-paulo/moema?page=7", fonte2="", x=None, y=None)
ref(id="R09", nome="The Frame Vila Nova Conceição", segmento="Pronto com estoque", incorporadora="", endereco="Vila Nova Conceição",
    status_obra="Pronto (Apto)", metragens="359", entrega="", distancia_aprox="a medir",
    obs="Listado como pronto no Apto. Estoque não confirmado.", fonte1="https://apto.vc/br/sp/sao-paulo/moema?page=7", fonte2="", x=None, y=None)
ref(id="R10", nome="Atmos Moema", segmento="Pronto com estoque", incorporadora="", endereco="a confirmar",
    status_obra="Pronto (Apto, 'últimas unidades')", metragens="160 a 345", entrega="", distancia_aprox="a medir",
    obs="Apto marca 'últimas unidades'.", fonte1="https://apto.vc/br/sp/sao-paulo/moema?page=5", fonte2="", x=None, y=None)
ref(id="R11", nome="Copa", segmento="Pronto com estoque", incorporadora="", endereco="Indianópolis",
    status_obra="Pronto (Apto)", metragens="301", entrega="", distancia_aprox="a medir",
    obs="Listado como pronto no Apto. Estoque não confirmado.", fonte1="https://apto.vc/br/sp/sao-paulo/moema?page=7", fonte2="", x=None, y=None)

# Candidatos a verificar (provavelmente fora do 2º anel ou sem dados suficientes)
VERIF = [
    dict(nome="Quarten Ibirapuera (Trisul)", motivo="Duplex de 306 e 395 m²; Av. Dr. Altino Arantes (Vila Clementino). Medir se está a menos de 2 km.", fonte="https://jornaldobras.com.br/noticia/102065/quarten-ibirapuera-integra-natureza-exclusividade-e-bem-estar-em-um-dos-enderecos-mais-desejados-de-sao-paulo"),
    dict(nome="The View Ibirapuera", motivo="Torre única de 290 m², Av. Prof. Ascendino Reis, 585. Status de venda não confirmado.", fonte="https://myside.com.br/apartamento-venda-the-view-ibirapuera-sao-paulo-sp"),
    dict(nome="Mairin Ibirapuera", motivo="Plantas de 179 a 379 m² (bairro Ibirapuera). Endereço e status a confirmar.", fonte="https://myside.com.br/apartamentos-venda-ibirapuera-sao-paulo-sp"),
    dict(nome="Hóriz Ibirapuera", motivo="Plantas de 231 e 301 m² com vista para o parque. Endereço e status a confirmar.", fonte="https://myside.com.br/apartamentos-venda-ibirapuera-sao-paulo-sp"),
    dict(nome="Breve lançamento Av. Chibarás", motivo="Plantas de 180 e 250 m² (Apto). Incorporadora não divulgada.", fonte="https://apto.vc/br/sp/sao-paulo/moema?page=7"),
    dict(nome="Portrait Parque do Ibirapuera (Cyrela)", motivo="232 a 355 m², mas no Paraíso: provavelmente além de 2 km. Fora do estudo, salvo decisão contrária.", fonte="https://myside.com.br/apartamento-venda-portrait-parque-do-ibirapuera-sao-paulo-sp"),
]

# ---------------- TIPOLOGIAS ----------------
TIP = {
 "Q":   [298, 350, 395],
 "C01": [293, 373],
 "C02": [284, 345, 416, 442, 570, 649, 770],
 "C03": [311, 317, 621],
 "C04": [317],
 "C05": [258],
 "C06": [215, 290, 381, 424, 572],
 "C07": [373, 453, 1185],
 "C08": [330, 430, 470],
 "C09": [336, 431, 851],
 "C10": [267, 530],
 "C11": [251],
 "C12": [256],
 "C13": [353, 395, 654],
 "C14": [247, 290, 332, 356, 380, 572],
 "C15": [208, 447],
 "C16": [476],
 "C17": [277, 320, 500],
 "C18": [264],
 "C19": [259],
}
def faixa(m):
    if m < 260: return "Abaixo (200-259)"
    if m <= 320: return "A (260-320)"
    if m <= 380: return "B (321-380)"
    if m <= 480: return "C (381-480)"
    return "D (acima de 480)"

# ---------------- ATRIBUTOS ----------------
# ✓ sim | ✗ não consta | ? sem informação
ATTR_COLS = ["Unid./andar", "Elevador ou hall privativo", "Quadra de tênis", "Piscina coberta", "Raia / comprimento", "Academia (marca)", "Varejo no térreo", "Torre única"]
ATTR = {
 "Q":   ["2", "✓ elevador privativo", "✓ saibro, oficial", "✓", "✓ 25 m", "✓ Technogym", "✓ GPA, acesso independente", "✓"],
 "C01": ["?", "?", "✓ (tipo ?)", "✓", "?", "?", "✗", "✓"],
 "C02": ["1 (na planta 416)", "✓ hall privativo", "✓ (tipo ?)", "✓", "✓ raia (comprimento ?)", "?", "✗", "divergente"],
 "C03": ["?", "?", "?", "?", "?", "?", "subcondomínio de studios", "✗ (2 torres)"],
 "C04": ["1", "✓ elevador delivery exclusivo", "✗ (quadra esportiva)", "✓", "?", "?", "✗", "✓"],
 "C05": ["?", "✓ hall privativo", "✓ Lisonda (sintético)", "?", "✓ 20 m", "✓ Life Fitness", "✗", "✓"],
 "C06": ["2", "?", "?", "?", "✓ semiolímpica (25 m)", "?", "✓ 1 loja", "✓"],
 "C07": ["2", "✓ hall privativo", "✓ (tipo ?)", "✓", "?", "?", "✗", "✓"],
 "C08": ["?", "?", "?", "?", "?", "?", "?", "✓"],
 "C09": ["?", "?", "?", "?", "?", "?", "?", "✓"],
 "C10": ["?", "?", "✗ não consta", "✗ não consta", "?", "✓ (marca ?)", "?", "✓"],
 "C11": ["?", "?", "?", "?", "?", "?", "?", "✓"],
 "C12": ["?", "✓ hall privativo", "?", "?", "?", "?", "?", "✗ (3 torres)"],
 "C13": ["?", "?", "?", "?", "?", "?", "?", "?"],
 "C14": ["2", "?", "✓ + beach tennis", "?", "?", "?", "?", "?"],
 "C15": ["?", "?", "?", "?", "?", "?", "?", "✓"],
 "C16": ["?", "?", "?", "?", "?", "?", "?", "✓"],
 "C17": ["?", "✓ hall privativo", "?", "?", "?", "?", "?", "✗"],
 "C18": ["?", "?", "✓ (tipo ?)", "?", "?", "?", "?", "✓"],
 "C19": ["?", "?", "?", "?", "?", "?", "?", "✓"],
}

# ---------------- PREÇOS (estudo Yuny fev/26 como base; colunas do Rogerio vazias) ----------------
PRECO_FEV_OLD = {  # lançamento, tabela atualizada, % vendido (estudo Yuny fev/26)
 "C01": ("32.500", "35.000", "3S 95% / 4S 70%"),
 "C03": ("27.000", "42.000", "65%"),
 "C04": ("32.000", "35.000", "90%"),
 "C05": ("30.000", "37.000", "4S-3v 50% / 4S-4v 85%"),
 "C06": ("29.000", "30.850", "3S 55% / 4S 48%"),
 "C07": ("50.000", "", "22%"),
 "C08": ("42.000", "", ""),
 "C09": ("45.000", "", ""),
}

PRECO_FEV = {}
# ---------------- BATTLE CARDS (rascunho para validação) ----------------
BC = []
def bc(pid, tipo, titulo, texto, base):
    BC.append(dict(id=pid, tipo=tipo, titulo=titulo, texto=texto, base=base))

bc("C01","Vulnerabilidade","Salto de 293 para 373 m²","Não há planta intermediária: quem precisa de mais que 293 m² e não quer 373 m² fica sem opção. O Quaddra tem ~350 m².","Tipologias publicadas (Apto, MySide)")
bc("C01","Ataque contra nós","Mesma quadra, um ano na frente","Lançou em 11/2025 com entrega em 11/2028: obra mais adiantada no mesmo endereço, com tênis e piscina coberta.","Apto: lançamento 11/2025, entrega 11/2028")
bc("C01","Resposta","Mais opções de planta e unidades especiais","Três plantas (~298, ~350 e ~395 m²) contra duas. As 9 unidades de ~395 m² não têm equivalente no vizinho.","Base Quaddra")
bc("C02","Vulnerabilidade","Entrega em 2030 ou depois","Os portais indicam entrega entre 02/2030 e 12/2031, a mais distante entre os diretos.","MySide e Apto")
bc("C02","Ataque contra nós","Mix maior e lazer equivalente","Duplex e casas suspensas de até 770 m², piscina com raia, piscina coberta e tênis, com a marca Cyrela.","MySide")
bc("C02","Resposta","Varejo próprio no térreo","Loja GPA com acesso independente: conveniência que o La Galerie não oferece. Validar se o prazo de entrega do Quaddra é anterior.","Base Quaddra")
bc("C03","Vulnerabilidade","Terreno compartilhado com studios","O terreno abriga subcondomínios independentes, incluindo uma torre de studios (Studio Sabiá), segundo o laudo da Kinea.","Laudo Kinea, out/2024")
bc("C03","Ataque contra nós","Pronto em 2027","Com entrega em 08/2027, vai vender como imóvel pronto enquanto o Quaddra estiver na planta.","Estudo Yuny fev/26")
bc("C03","Resposta","Torre única residencial","Quaddra: uma torre residencial, 2 por andar, sem studios no mesmo terreno.","Base Quaddra")
bc("C04","Vulnerabilidade","Planta única de 317 m²","Quem precisa de mais área não tem alternativa no Singular.","MySide")
bc("C04","Ataque contra nós","Um apartamento por andar","28 unidades, uma por andar, com elevador delivery exclusivo: mais privacidade que 2 por andar.","MySide")
bc("C04","Resposta","Lazer de clube","Tênis oficial de saibro e raia de 25 m; o Singular lista quadra esportiva, sem quadra de tênis.","MySide (lista de lazer)")
bc("C05","Vulnerabilidade","Metragem única e menor","Só 258 m², abaixo da menor planta do Quaddra.","MySide")
bc("C05","Ataque contra nós","Pronto antes e ticket menor","Entrega em 10/2027 e ticket total menor por ter só 258 m².","MySide")
bc("C05","Resposta","Lazer superior","Raia de 25 m contra piscina de 20 m; saibro contra quadra sintética (Lisonda).","MySide")
bc("C06","Vulnerabilidade","Sem quadra de tênis listada","A lista de lazer publicada não traz quadra de tênis.","MySide")
bc("C06","Ataque contra nós","Piscina semiolímpica e EZTEC","Piscina semiolímpica (25 m) e plantas de 381 a 572 m² com a solidez da EZTEC.","MySide, RI EZTEC")
bc("C06","Resposta","Tênis oficial e varejo","Tênis oficial de saibro e loja GPA no térreo. Raia equivalente (25 m).","Base Quaddra")
bc("C07","Vulnerabilidade","Ticket mais alto da região","Plantas a partir de 373 m² de frente para o parque: o ticket total mais alto entre os diretos (valores em atualização).","MySide (metragens)")
bc("C07","Ataque contra nós","Vista definitiva do parque","Frente para o Parque Ibirapuera, 2 por andar, piscina coberta e tênis.","MySide")
bc("C07","Resposta","Mesmo padrão de planta, ticket menor","Plantas de 350 e 395 m² num bairro residencial, com ticket a confirmar quando os preços forem atualizados.","A validar com os preços atualizados")
bc("C08","Vulnerabilidade","Entrega só em 2031","Entrega prevista para 02/2031.","MySide")
bc("C08","Ataque contra nós","Demanda comprovada","Vendeu mais da metade das 75 unidades nos primeiros dias, com VGV de R$ 1,2 bi.","Imprensa")
bc("C08","Resposta","Prazo (a confirmar)","Se a entrega do Quaddra for anterior a 2031, esse é o argumento.","A definir")
bc("C13","Vulnerabilidade","Condomínio alto","A Trisul estima condomínio de R$ 6 a 7 mil por mês.","Money Times / Estadão")
bc("C13","Ataque contra nós","Escala e plantas grandes","Terreno de 6.289 m² e unidades de até 654 m².","Money Times; jul/26")
bc("C13","Resposta","A definir","Depende do condomínio estimado do Quaddra.","A definir")
bc("C10","Vulnerabilidade","Lazer enxuto","A lista de lazer publicada traz academia, piscina adulto e hidromassagem, sem tênis nem piscina coberta.","Apto")
bc("C10","Ataque contra nós","Plantas de 267 e 530 m²","Pega o cliente abaixo da nossa menor planta e o cliente de duplex.","Apto")
bc("C10","Resposta","Clube completo","Tênis oficial, raia de 25 m, Technogym e loja GPA.","Base Quaddra")
bc("C14","Vulnerabilidade","Público misto na mesma torre","As plantas vão de 177 a 572 m² no mesmo prédio.","MySide")
bc("C14","Ataque contra nós","Pronto em 2026, com tênis","Entrega em 10/2026, 2 por andar, quadra de tênis e beach tennis.","MySide, Apto")
bc("C14","Resposta","Localização","Moema Pássaros, em frente ao Lindenberg, contra Av. Indianópolis.","A validar")


def dist(p):
    if p.get("x") is None: return None
    return int(round(math.hypot(p["x"], p["y"]) / 10.0) * 10)

ORIG = "Avenida Sabiá, Moema, São Paulo - SP"
def gmaps(addr):
    return "https://www.google.com/maps/dir/?api=1&travelmode=walking&origin=" + urllib.parse.quote(ORIG) + "&destination=" + urllib.parse.quote(addr + ", São Paulo - SP")

for p in P:
    p["dist_m"] = dist(p)
    p["dist_txt"] = ("≈ %s m" % format(p["dist_m"], ",").replace(",", ".")) + (" (estimada)" if p["pos_base"] == "estimada" else " (mapa)")
    p["gmaps"] = gmaps(p["endereco"])
    p["tipologias"] = TIP.get(p["id"], [])
    p["faixas"] = sorted(set(("<A" if m < 260 else faixa(m)[0]) for m in p["tipologias"]), key=lambda c: "0" if c=="<A" else c)
    p["atributos"] = ATTR.get(p["id"], ["?"] * len(ATTR_COLS))
    pf = PRECO_FEV.get(p["id"], ("", "", ""))
    p["preco_lanc_fev"], p["preco_tab_fev"], p["vendido_fev"] = pf
QUADDRA["tipologias"] = TIP["Q"]; QUADDRA["atributos"] = ATTR["Q"]; QUADDRA["dist_m"] = 0
for r in REF:
    r["gmaps"] = gmaps(r["endereco"]) if "confirmar" not in r["endereco"] else ""

out = dict(data=DATA_CHECAGEM, quaddra=QUADDRA, projetos=P, referencia=REF, verificar=VERIF,
           attr_cols=ATTR_COLS, battle=BC,
           faixas=[["A", "260-320", "~298 m²"], ["B", "321-380", "~350 m²"], ["C", "381-480", "~395 m²"], ["D", "acima de 480", "duplex e coberturas"]])
json.dump(out, open("/home/claude/quaddra/data.json", "w"), ensure_ascii=False, indent=1)

# ---------- linhas para o Sheets ----------
S = {}
hdr = ["ID","Empreendimento","Também chamado","Incorporadora","Endereço","Anel","Distância aprox. (m)","Base da distância","Rota a pé (Google Maps)","Status da obra","Lançamento","Entrega","Torres","Pavimentos","Unidades","Unid./andar","Terreno (m²)","m² de terreno por unidade","Metragens (m²)","Faixas","Suítes","Vagas","Arquitetura","Paisagismo","Interiores","VGV","Presença nos estudos Yuny","Status do dado","Observações e divergências","Fonte 1","Fonte 2"]
rows = [hdr]
def num(s):
    try: return float(str(s).replace(".", "").replace(",", "."))
    except: return ""
allp = [QUADDRA] + P
for i, p in enumerate(allp):
    r = i + 2
    uni = p.get("unidades", "")
    terr = num(p.get("terreno", ""))
    rows.append([p["id"], p["nome"], p.get("alias",""), p["incorporadora"], p["endereco"], p["anel"],
                 p.get("dist_m", "") if p["id"] != "Q" else 0,
                 {"mapa":"Medida no mapa dos estudos Yuny (±100 m)","estimada":"Estimada pelo endereço (±300-400 m)"}.get(p.get("pos_base"),""),
                 ('=HYPERLINK("%s","abrir rota")' % p["gmaps"]) if p.get("gmaps") else "",
                 p["status_obra"], "'" + p["lancamento"] if p["lancamento"] else "", "'" + p["entrega"] if p["entrega"] else "",
                 "'" + p["torres"] if p["torres"] else "", p["pavimentos"], p["unidades"], "'" + p["unid_andar"] if p["unid_andar"] else "",
                 terr,
                 '=IFERROR(Q%d/VALUE(REGEXEXTRACT(TO_TEXT(O%d),"^\\d+")),"")' % (r, r),
                 p["metragens"], ", ".join(p.get("faixas", [])), p["suites"], p["vagas"],
                 p["arquitetura"], p["paisagismo"], p["interiores"], p["vgv"], p["estudos_yuny"], p["status_dado"], p["obs"], p["fonte1"], p["fonte2"]])
S["Projetos"] = rows

rows = [["ID","Empreendimento","Metragem (m²)","Faixa","Faixa do Quaddra equivalente"]]
r = 2
for p in allp:
    for m in TIP.get(p["id"], []):
        rows.append([p["id"], p["nome"], m,
                     '=IF(C{r}<260,"Abaixo (200-259)",IF(C{r}<=320,"A (260-320)",IF(C{r}<=380,"B (321-380)",IF(C{r}<=480,"C (381-480)","D (acima de 480)"))))'.format(r=r),
                     '=IF(C{r}<260,"menor que a menor planta",IF(C{r}<=320,"~298 m²",IF(C{r}<=380,"~350 m²",IF(C{r}<=480,"~395 m²","duplex / cobertura"))))'.format(r=r)])
        r += 1
S["Tipologias"] = rows

rows = [["ID","Empreendimento"] + ATTR_COLS + ["Fonte"]]
for p in allp:
    rows.append([p["id"], p["nome"]] + ATTR.get(p["id"], ["?"]*len(ATTR_COLS)) + [p.get("fonte1","")])
S["Atributos"] = rows

rows = [["ID","Empreendimento","Lançamento R$/m² (estudo fev/26)","Tabela R$/m² (estudo fev/26)","% vendido (estudo fev/26)","Tabela atual R$/m²","Data da tabela","Fonte da tabela","Fechamento real R$/m²","Data do fechamento","Fonte do fechamento","Desconto sobre tabela","% vendido atual","Data do % vendido","Observações"]]
for i, p in enumerate(allp):
    r = i + 2
    pf = PRECO_FEV.get(p["id"], ("","",""))
    lanc = num(pf[0]) if pf[0] else ""
    tab = num(pf[1]) if pf[1] else ""
    if p["id"] == "Q":
        rows.append([p["id"], p["nome"], 32000, "", "", "", "", "", "", "", "", '=IF(OR(F%d="",I%d=""),"",1-I%d/F%d)' % (r,r,r,r), "", "", "Preço médio de lançamento estimado (base interna)"])
    else:
        rows.append([p["id"], p["nome"], lanc, tab, pf[2], "", "", "", "", "", "", '=IF(OR(F%d="",I%d=""),"",1-I%d/F%d)' % (r,r,r,r), "", "", ""])
S["Preços"] = rows

rows = [["ID","Empreendimento","Tipo","Título","Texto","Base factual","Validado?"]]
nm = {p["id"]: p["nome"] for p in allp}
for b in BC:
    rows.append([b["id"], nm[b["id"]], b["tipo"], b["titulo"], b["texto"], b["base"], "Não"])
S["Battle cards"] = rows

rows = [["ID","Empreendimento","Segmento","Incorporadora","Endereço","Status","Metragens (m²)","Entrega","Distância aprox.","Observações","Fonte 1","Fonte 2"]]
for x in REF:
    rows.append([x["id"], x["nome"], x["segmento"], x["incorporadora"], x["endereco"], x["status_obra"], x["metragens"], "'" + x["entrega"] if x["entrega"] else "", x["distancia_aprox"], x["obs"], x["fonte1"], x["fonte2"]])
rows.append([]); rows.append(["A verificar (podem entrar no estudo)"])
rows.append(["","Empreendimento","Motivo","","","","","","","","Fonte",""])
for v in VERIF:
    rows.append(["", v["nome"], v["motivo"], "", "", "", "", "", "", "", v["fonte"], ""])
S["Referência"] = rows

rows = [["Estudo de concorrência Quaddra Sabiá: produtos de 200 m² ou mais"],
        ["Checagem dos dados: " + DATA_CHECAGEM],
        [""],
        ["Abas"],
        ["Projetos", "Uma linha por concorrente: ficha técnica, anel, distância, status do dado e fontes."],
        ["Tipologias", "Uma linha por planta, classificada na faixa equivalente do Quaddra."],
        ["Atributos", "Matriz de diferenciais: ✓ consta na fonte, ✗ não consta ou não tem, ? sem informação."],
        ["Preços", "Colunas F a O são de preenchimento manual (tabela e fechamento real). C a E vêm do estudo Yuny de fev/2026."],
        ["Battle cards", "Rascunho: vulnerabilidade deles, como atacam o Quaddra, resposta. Marcar 'Validado?' antes de usar."],
        ["Referência", "Prontos com estoque, esgotados e produtos acima da faixa, mais a lista de candidatos a verificar."],
        [""],
        ["Critérios"],
        ["Anel 1", "Até 1 km do Quaddra."],
        ["Anel 2", "De 1 a 2 km."],
        ["Faixas", "A 260-320 m² (~298) | B 321-380 m² (~350) | C 381-480 m² (~395) | D acima de 480 m² (duplex e coberturas)."],
        ["Distância", "Medida nos mapas dos estudos Yuny (±100 m) ou estimada pelo endereço (±300-400 m). Validar pela rota do Google Maps de cada linha."],
        [""],
        ["Status do dado"],
        ["Confirmado (2 fontes)", "Dado batido em duas fontes independentes ou fonte oficial (RI)."],
        ["1 fonte por dado", "Só uma fonte pública encontrada."],
        ["Divergente", "Fontes discordam; detalhe em Observações."],
        ]
S["Leia-me"] = rows
json.dump(S, open("/home/claude/quaddra/sheets.json", "w"), ensure_ascii=False)
print("projetos", len(P), "ref", len(REF), "tip rows", len(S["Tipologias"])-1, "bc", len(BC))
for p in P:
    print(p["id"], p["nome"], p["anel"], p["dist_m"], p["pos_base"], p["faixas"])
