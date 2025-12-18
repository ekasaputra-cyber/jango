document.addEventListener('DOMContentLoaded', async () => {
    const container = document.getElementById('warga-list-container');
    const apiUrl = 'http://127.0.0.1:8000/api/pengaduan/';
    const token = localStorage.getItem('authToken');

    if (!token) {
        container.innerHTML = `
            <div class="alert alert-warning text-center">
                Silakan login terlebih dahulu
            </div>
        `;
        return;
    }

    function escapeHtml(str) {
        return String(str ?? '')
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#39;');
    }

    function renderTableRow(item, index) {
        return `
            <tr>
                <td>${index + 1}</td>
                <td>${escapeHtml(item.judul)}</td>
                <td>${escapeHtml(item.isi)}</td>
                <td>${escapeHtml(item.created_at || '-')}</td>
                <td>
                    <span class="badge ${item.status === 'BARU' ? 'bg-primary' :
                                        item.status === 'DIPROSES' ? 'bg-warning text-dark' :
                                        item.status === 'SELESAI' ? 'bg-success' : 'bg-secondary'}">
                        ${escapeHtml(item.status)}
                    </span>
                </td>
            </tr>
        `;
    }

    container.innerHTML = `
        <div class="d-flex justify-content-center my-5">
            <div class="spinner-border text-primary"></div>
        </div>
    `;

    try {
        const resp = await fetch(apiUrl, {
            headers: { 'Authorization': 'Token ' + token }
        });

        if (!resp.ok) throw new Error(resp.status);

        const data = await resp.json();
        const list = data.results || [];

        if (list.length === 0) {
            container.innerHTML = `
                <div class="alert alert-info text-center">
                    Belum ada data pengaduan
                </div>
            `;
            return;
        }

        let html = `
            <div class="table-responsive">
                <table class="table table-bordered table-striped">
                    <thead class="table-dark">
                        <tr>
                            <th>No</th>
                            <th>Judul</th>
                            <th>Isi</th>
                            <th>Tanggal</th>
                            <th>Status</th>
                        </tr>
                    </thead>
                    <tbody>
        `;

        list.forEach((item, idx) => {
            html += renderTableRow(item, idx);
        });

        html += `
                    </tbody>
                </table>
            </div>
        `;

        container.innerHTML = html;

    } catch (err) {
        console.error(err);
        container.innerHTML = `
            <div class="alert alert-danger text-center">
                Gagal memuat data pengaduan
            </div>
        `;
    }
});
