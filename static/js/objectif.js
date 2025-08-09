// JavaScript pour la page des objectifs

document.addEventListener('DOMContentLoaded', function() {
    // Éléments DOM
    const addObjectifBtn = document.getElementById('addObjectifBtn');
    const objectifModal = document.getElementById('objectifModal');
    const closeBtn = objectifModal.querySelector('.close-btn');
    const cancelObjectifBtn = document.getElementById('cancelObjectifBtn');
    const objectifForm = document.getElementById('objectifForm');
    const objectifFilter = document.getElementById('objectifFilter');
    const modalTitle = objectifModal.querySelector('.modal-title');
    
    // Données pour le graphique
    const objectifsData = {
        labels: ['Vacances d\'été', 'Remboursement Prêt Auto', 'Fonds d\'urgence', 'Limitation restaurant'],
        datasets: [{
            label: 'Progression (%)',
            data: [75, 60, 90, 40],
            backgroundColor: [
                'rgba(67, 97, 238, 0.6)',
                'rgba(247, 37, 133, 0.6)',
                'rgba(67, 97, 238, 0.6)',
                'rgba(76, 201, 240, 0.6)'
            ],
            borderColor: [
                'rgba(67, 97, 238, 1)',
                'rgba(247, 37, 133, 1)',
                'rgba(67, 97, 238, 1)',
                'rgba(76, 201, 240, 1)'
            ],
            borderWidth: 1
        }]
    };

    // Initialiser le graphique
    const ctx = document.getElementById('objectifsChart').getContext('2d');
    const objectifsChart = new Chart(ctx, {
        type: 'bar',
        data: objectifsData,
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true,
                    max: 100,
                    ticks: {
                        callback: function(value) {
                            return value + '%';
                        }
                    }
                }
            },
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return context.raw + '%';
                        }
                    }
                }
            }
        }
    });

    // Ouvrir modal pour ajouter un objectif
    addObjectifBtn.addEventListener('click', function() {
        modalTitle.textContent = 'Ajouter un objectif';
        objectifForm.reset();
        objectifModal.style.display = 'block';
    });

    // Fermer modal
    function closeModal() {
        objectifModal.style.display = 'none';
    }

    closeBtn.addEventListener('click', closeModal);
    cancelObjectifBtn.addEventListener('click', closeModal);

    // Fermer modal si clic en dehors
    window.addEventListener('click', function(event) {
        if (event.target === objectifModal) {
            closeModal();
        }
    });

    // Soumettre le formulaire
    objectifForm.addEventListener('submit', function(event) {
        event.preventDefault();
        
        // Récupérer les valeurs du formulaire
        const title = document.getElementById('objectifTitle').value;
        const category = document.getElementById('objectifCategory').value;
        const amount = document.getElementById('objectifAmount').value;
        const currentAmount = document.getElementById('objectifCurrentAmount').value;
        const date = document.getElementById('objectifDate').value;
        
        // Dans un environnement réel, vous enverriez ces données à votre backend
        console.log('Nouvel objectif:', {
            title,
            category,
            amount,
            currentAmount,
            date
        });
        
        // Fermer le modal
        closeModal();
        
        // Dans un environnement réel, vous rechargeriez les données ou ajouteriez l'objectif au DOM
        alert('Objectif enregistré avec succès!');
    });

    // Filtre des objectifs
    objectifFilter.addEventListener('change', function() {
        const filterValue = this.value;
        const objectifCards = document.querySelectorAll('.objectif-card');
        
        objectifCards.forEach(card => {
            const categoryElement = card.querySelector('.objectif-category');
            const categoryValue = categoryElement.classList[1]; // 'saving', 'spending', 'debt'
            
            if (filterValue === 'all' || categoryValue === filterValue) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    });

    // Gestion des boutons d'édition
    document.querySelectorAll('.action-btn.edit').forEach(btn => {
        btn.addEventListener('click', function() {
            const objectifId = this.getAttribute('data-id');
            
            // Dans un environnement réel, vous récupéreriez les données de l'objectif
            // À des fins de démonstration, nous utilisons des valeurs codées en dur
            const demoData = {
                1: {
                    title: 'Vacances d\'été',
                    category: 'saving',
                    amount: 2000,
                    currentAmount: 1500,
                    date: '2025-07-15',
                    notes: 'Voyage à Barcelone'
                },
                2: {
                    title: 'Remboursement Prêt Auto',
                    category: 'debt',
                    amount: 10000,
                    currentAmount: 6000,
                    date: '2025-12-10',
                    notes: 'Prêt auto sur 3 ans'
                },
                3: {
                    title: 'Fonds d\'urgence',
                    category: 'saving',
                    amount: 5000,
                    currentAmount: 4500,
                    date: '2025-05-31',
                    notes: '3 mois de dépenses'
                },
                4: {
                    title: 'Limitation restaurant',
                    category: 'spending',
                    amount: 100,
                    currentAmount: 120,
                    date: '2025-05-31',
                    notes: 'Limiter les sorties au restaurant en mai'
                }
            };
            
            const objectifData = demoData[objectifId];
            
            // Remplir le formulaire avec les données
            document.getElementById('objectifTitle').value = objectifData.title;
            document.getElementById('objectifCategory').value = objectifData.category;
            document.getElementById('objectifAmount').value = objectifData.amount;
            document.getElementById('objectifCurrentAmount').value = objectifData.currentAmount;
            document.getElementById('objectifDate').value = objectifData.date;
            document.getElementById('objectifNotes').value = objectifData.notes;
            
            // Changer le titre du modal
            modalTitle.textContent = 'Modifier l\'objectif';
            
            // Afficher le modal
            objectifModal.style.display = 'block';
        });
    });

    // Gestion des boutons de suppression
    document.querySelectorAll('.action-btn.delete').forEach(btn => {
        btn.addEventListener('click', function() {
            const objectifId = this.getAttribute('data-id');
            const confirmDelete = confirm('Êtes-vous sûr de vouloir supprimer cet objectif ?');
            
            if (confirmDelete) {
                // Dans un environnement réel, vous enverriez une requête pour supprimer l'objectif
                console.log('Supprimer objectif ID:', objectifId);
                
                // Simuler la suppression de l'interface utilisateur
                this.closest('.objectif-card').style.opacity = '0.5';
                setTimeout(() => {
                    this.closest('.objectif-card').remove();
                }, 500);
                
                alert('Objectif supprimé avec succès!');
            }
        });
    });
});