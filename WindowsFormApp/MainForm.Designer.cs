namespace WindowsFormApp
{
    partial class MainForm
    {
        /// <summary>
        /// 必需的设计器变量。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清理所有正在使用的资源。
        /// </summary>
        /// <param name="disposing">如果应释放托管资源，为 true；否则为 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows 窗体设计器生成的代码

        /// <summary>
        /// 设计器支持所需的方法 - 不要修改
        /// 使用代码编辑器修改此方法的内容。
        /// </summary>
        private void InitializeComponent()
        {
            this.buttonAddToList = new System.Windows.Forms.Button();
            this.listBoxTimes = new System.Windows.Forms.ListBox();
            this.SuspendLayout();
            // 
            // buttonAddToList
            // 
            this.buttonAddToList.Location = new System.Drawing.Point(34, 40);
            this.buttonAddToList.Name = "buttonAddToList";
            this.buttonAddToList.Size = new System.Drawing.Size(75, 23);
            this.buttonAddToList.TabIndex = 0;
            this.buttonAddToList.Text = "AddToList";
            this.buttonAddToList.UseVisualStyleBackColor = true;
            // 
            // listBoxTimes
            // 
            this.listBoxTimes.FormattingEnabled = true;
            this.listBoxTimes.ItemHeight = 12;
            this.listBoxTimes.Location = new System.Drawing.Point(149, 40);
            this.listBoxTimes.Name = "listBoxTimes";
            this.listBoxTimes.Size = new System.Drawing.Size(321, 280);
            this.listBoxTimes.TabIndex = 1;
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(502, 353);
            this.Controls.Add(this.listBoxTimes);
            this.Controls.Add(this.buttonAddToList);
            this.Name = "MainForm";
            this.Text = "MainForm";
            this.ResumeLayout(false);

        }

        #endregion

        public System.Windows.Forms.Button buttonAddToList;
        public System.Windows.Forms.ListBox listBoxTimes;
    }
}

