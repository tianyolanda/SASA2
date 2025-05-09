报错
eval:   0%|          | 0/1885 [00:00<?, ?it/s]/home/ubuntu/codes/2025codes/SASA2/pcdet/utils/density_calculation.py:73: UserWarning: To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() or sourceTensor.clone().detach().requires_grad_(True), rather than torch.tensor(sourceTensor).

Backend QtAgg is interactive backend. Turning interactive mode on.
qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

Available platform plugins are: eglfs, linuxfb, minimal, minimalegl, offscreen, vnc, wayland-egl, wayland, wayland-xcomposite-egl, wayland-xcomposite-glx, webgl, xcb.


解决:
matplotlib.use('TkAgg')

