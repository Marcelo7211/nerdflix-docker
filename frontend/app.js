// O front chama a API pelo mesmo endereço da página (/api/...).
// Em produção quem entrega essa rota é o Nginx, que faz proxy para o container da API.
const lista = document.getElementById('lista-filmes')
const status = document.getElementById('status')
const versao = document.getElementById('versao')
const formulario = document.getElementById('form-filme')

function mostrarErro(mensagem) {
  status.textContent = mensagem
  status.classList.add('erro')
}

async function carregarFilmes() {
  try {
    const resposta = await fetch('/api/filmes')
    if (!resposta.ok) throw new Error('API respondeu ' + resposta.status)
    const filmes = await resposta.json()
    lista.innerHTML = ''
    filmes.forEach((filme) => {
      const item = document.createElement('li')
      item.innerHTML = '<span></span><span class="ano"></span>'
      item.children[0].textContent = filme.titulo
      item.children[1].textContent = filme.ano
      lista.appendChild(item)
    })
    status.classList.remove('erro')
    status.textContent = filmes.length + ' filme(s) no catálogo'
  } catch (erro) {
    lista.innerHTML = ''
    mostrarErro('API indisponível por enquanto. Suba o back-end e o banco para ver os filmes.')
  }
}

async function carregarVersao() {
  try {
    const resposta = await fetch('/api/saude')
    const dados = await resposta.json()
    versao.textContent = 'API versão ' + dados.versao + ' respondendo pelo container ' + dados.host
  } catch (erro) {
    versao.textContent = 'API: sem resposta'
  }
}

formulario.addEventListener('submit', async (evento) => {
  evento.preventDefault()
  const corpo = {
    titulo: document.getElementById('titulo-filme').value,
    ano: Number(document.getElementById('ano-filme').value)
  }
  const resposta = await fetch('/api/filmes', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(corpo)
  })
  if (resposta.ok) {
    formulario.reset()
    carregarFilmes()
  } else {
    mostrarErro('Não foi possível cadastrar o filme.')
  }
})

carregarFilmes()
carregarVersao()
