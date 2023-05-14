
Partie 1:
<script>
  // Système d'authentification
  function auth() {
    if (
      document.getElementById("username").value === "admin" &&
      document.getElementById("password").value === "h5cf8gf2s5q7d"
    ) {
      window.location.href = "/fable/partie-2-cookie";
    }
  }
</script>
dans inspecter l'elemeent

Partie 2:
On vas dans cookie: on passe isAdmin de false a true

Partie 3:
On vas dans Timeline:
--> Partie4...-->Script evalued

On tombe sur:
<div>Flag : 404CTF{N0_frOn1_3nD_auTh3nt1ficAti0n}</div>
<script>
  const queryString = window.location.search;
  const urlParams = new URLSearchParams(queryString);
  if (urlParams.has("username") && urlParams.has("password")) {
    const username = urlParams.get("username");
    const password = urlParams.get("password");
    if (!(username === "admin" && password === "Fbqh96BthQ")) {
      document.location = "/fable/partie-3-redirect";
    }
  } else {
    document.location = "/fable/partie-3-redirect";
  }
</script>






404CTF{N0_frOn1_3nD_auTh3nt1ficAti0n}
