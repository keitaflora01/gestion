
        // // Initialize Chart
        // const ctx = document.getElementById('expenseChart').getContext('2d');
        // const expenseChart = new Chart(ctx, {
        //     type: 'line',
        //     data: {
        //         labels: ['Jan', 'Fév', 'Mar', 'Avr', 'Mai'],
        //         datasets: [{
        //             label: 'Dépenses',
        //             data: [1100, 1250, 1320, 1180, 1250],
        //             borderColor: '#f72585',
        //             backgroundColor: 'rgba(247, 37, 133, 0.1)',
        //             tension: 0.3,
        //             fill: true
        //         }, {
        //             label: 'Revenus',
        //             data: [2800, 2800, 2850, 2800, 2800],
        //             borderColor: '#4cc9f0',
        //             backgroundColor: 'rgba(76, 201, 240, 0.1)',
        //             tension: 0.3,
        //             fill: true
        //         }]
        //     },
        //     options: {
        //         responsive: true,
        //         maintainAspectRatio: false,
        //         scales: {
        //             y: {
        //                 beginAtZero: true,
        //                 ticks: {
        //                     callback: function(value) {
        //                         return value + ' €';
        //                     }
        //                 }
        //             }
        //         }
        //     }
        // });
        
        // // Modal functionality
        // const modal = document.getElementById('expenseModal');
        // const addExpenseBtn = document.getElementById('addExpenseBtn');
        // const closeBtn = document.querySelector('.close-btn');
        // const cancelBtn = document.getElementById('cancelExpenseBtn');
        
        // addExpenseBtn.addEventListener('click', () => {
        //     modal.style.display = 'block';
        //     document.getElementById('expenseDate').valueAsDate = new Date();
        // });
        
        // closeBtn.addEventListener('click', () => {
        //     modal.style.display = 'none';
        // });
        
        // cancelBtn.addEventListener('click', () => {
        //     modal.style.display = 'none';
        // });
        
        // window.addEventListener('click', (e) => {
        //     if (e.target === modal) {
        //         modal.style.display = 'none';
        //     }
        // });
        
        // // Form submission
        // const expenseForm = document.getElementById('expenseForm');
        // const expenseTable = document.getElementById('expenseTable');
        
        // expenseForm.addEventListener('submit', (e) => {
        //     e.preventDefault();
            
        //     const date = document.getElementById('expenseDate').value;
        //     const category = document.getElementById('expenseCategory').value;
        //     const description = document.getElementById('expenseDescription').value;
        //     const amount = document.getElementById('expenseAmount').value;
            
        //     // Format date
        //     const formattedDate = new Date(date).toLocaleDateString('fr-FR');
            
        //     // Create new row
        //     const newRow = document.createElement('tr');
        //     newRow.innerHTML = `
        //         <td>${formattedDate}</td>
        //         <td>${category}</td>
        //         <td>${description}</td>
        //         <td>${parseFloat(amount).toFixed(2)} €</td>
        //         <td class="action-buttons">
        //             <button class="action-btn edit"><i>✏️</i></button>
        //             <button class="action-btn delete"><i>🗑️</i></button>
        //         </td>
        //     `;
            
        //     // Add to table
        //     expenseTable.insertBefore(newRow, expenseTable.firstChild);
            
        //     // Reset form and close modal
        //     expenseForm.reset();
        //     modal.style.display = 'none';
            
        //     // Add event listeners to new buttons
        //     addActionButtonListeners(newRow);
        // });
        
        // // Add event listeners to existing action buttons
        // function addActionButtonListeners(row) {
        //     const editBtn = row.querySelector('.edit');
        //     const deleteBtn = row.querySelector('.delete');
            
        //     editBtn.addEventListener('click', () => {
        //         const cells = row.querySelectorAll('td');
                
        //         // Parse date
        //         const dateParts = cells[0].textContent.split('/');
        //         const dateFormatted = `${dateParts[2]}-${dateParts[1]}-${dateParts[0]}`;
                
        //         // Fill form
        //         document.getElementById('expenseDate').value = dateFormatted;
        //         document.getElementById('expenseCategory').value = cells[1].textContent;
        //         document.getElementById('expenseDescription').value = cells[2].textContent;
        //         document.getElementById('expenseAmount').value = parseFloat(cells[3].textContent);
                
        //         // Open modal
        //         modal.style.display = 'block';
                
        //         // Remove the row (it will be re-added on form submission)
        //         row.remove();
        //     });
            
        //     deleteBtn.addEventListener('click', () => {
        //         if (confirm('Êtes-vous sûr de vouloir supprimer cette dépense ?')) {
        //             row.remove();
        //         }
        //     });
        // }
        
        // // Initialize action buttons
        // document.querySelectorAll('#expenseTable tr').forEach(addActionButtonListeners);
        
        // // Calculate total based on date range
        // const calculateTotalBtn = document.getElementById('calculateTotal');
        
        // calculateTotalBtn.addEventListener('click', () => {
        //     const startDate = new Date(document.getElementById('startDate').value);
        //     const endDate = new Date(document.getElementById('endDate').value);
            
        //     if (isNaN(startDate.getTime()) || isNaN(endDate.getTime())) {
        //         alert('Veuillez sélectionner des dates valides');
        //         return;
        //     }
            
        //     let total = 0;
            
        //     document.querySelectorAll('#expenseTable tr').forEach(row => {
        //         const dateCell = row.querySelector('td:first-child').textContent;
        //         const amountCell = row.querySelector('td:nth-child(4)').textContent;
                
        //         // Parse date
        //         const dateParts = dateCell.split('/');
        //         const rowDate = new Date(`${dateParts[2]}-${dateParts[1]}-${dateParts[0]}`);
                
        //         // Parse amount
        //         const amount = parseFloat(amountCell.replace('€', '').trim());
                
        //         // Check if date is in range
        //         if (rowDate >= startDate && rowDate <= endDate) {
        //             total += amount;
        //         }
        //     });
            
        //     alert(`Total des dépenses pour la période sélectionnée: ${total.toFixed(2)} €`);
        // });
        
        // // Chat functionality
        // const chatInput = document.getElementById('chatInput');
        // const sendMessageBtn = document.getElementById('sendMessageBtn');
        // const chatMessages = document.getElementById('chatMessages');
        
        // sendMessageBtn.addEventListener('click', sendMessage);
        // chatInput.addEventListener('keypress', (e) => {
        //     if (e.key === 'Enter') {
        //         sendMessage();
        //     }
        // });
        
        // function sendMessage() {
        //     const message = chatInput.value.trim();
        //     if (message === '') return;
            
        //     // Add user message
        //     const userMsg = document.createElement('div');
        //     userMsg.className = 'message user-message';
        //     userMsg.textContent = message;
        //     chatMessages.appendChild(userMsg);
            
        //     // Clear input
        //     chatInput.value = '';
            
        //     // Simulate AI response
        //     setTimeout(() => {
        //         const aiMsg = document.createElement('div');
        //         aiMsg.className = 'message ai-message';
                
        //         // Simple responses based on keywords
        //         if (message.toLowerCase().includes('dépens')) {
        //             aiMsg.textContent = "Vos dépenses totales ce mois-ci s'élèvent à 1250€. C'est 5% de moins que le mois dernier.";
        //         } else if (message.toLowerCase().includes('économ')) {
        //             aiMsg.textContent = "Vous économisez bien ! Vous avez mis de côté 1550€ ce mois-ci, soit 55% de vos revenus.";
        //         } else if (message.toLowerCase().includes('conseil')) {
        //             aiMsg.textContent = "Pour améliorer votre épargne, essayez de réduire vos dépenses en loisirs qui ont augmenté de 15