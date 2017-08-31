joint_list = []

joint_list.append([0.29067888855934143, -1.0801880995379847, 1.40675687789917, -2.754533116017477, 5.852528095245361, 0.9097236394882202])
joint_list.append([0.3461950421333313, -1.2442601362811487, 1.6534757614135742, -2.909239117299215, 5.809255123138428, 0.9896048903465271])
joint_list.append([0.5170721411705017, -1.520522419606344, 2.0111007690429688, -3.1417797247516077, 5.6643500328063965, 1.166231393814087])
joint_list.append([0.8365045189857483, -1.7258270422564905, 2.2163920402526855, -3.281149212514059, 5.372135162353516, 1.3560124635696411])
joint_list.append([1.4341109991073608, -1.7334197203265589, 2.22515869140625, -3.356386963521139, 4.801814079284668, 1.5512096881866455])
joint_list.append([1.8948371410369873, -1.5572412649737757, 2.0611000061035156, -3.3508413473712366, 4.358983039855957, 1.6815377473831177])
joint_list.append([1.8866873979568481, -1.6501358191119593, 1.4568133354187012, -2.6543262640582483, 4.366860389709473, 1.6785986423492432])
joint_list.append([1.5072170495986938, -1.7997410933123987, 1.5889906883239746, -2.6556199232684534, 4.731412887573242, 1.5708937644958496])
joint_list.append([1.1779849529266357, -1.8419035116778772, 1.6194648742675781, -2.626514259968893, 5.047666072845459, 1.4775980710983276])
joint_list.append([0.693164587020874, -1.742164436970846, 1.5377154350280762, -2.5390270392047327, 5.50534200668335, 1.2854058742523193])
joint_list.append([0.4470382034778595, -1.5011733214007776, 1.2978968620300293, -2.398966614400045, 5.726033687591553, 1.1064623594284058])
joint_list.append([0.32225507497787476, -1.1811755339251917, 0.879908561706543, -2.1712172667132776, 5.8284406661987305, 0.9586324095726013])

for i, js in enumerate(joint_list):
	s = '    <group_state name="code_{}" group="camera">\n\
        <joint name="ur5_shoulder_pan_joint" value="{}" />\n\
        <joint name="ur5_shoulder_lift_joint" value="{}" />\n\
        <joint name="ur5_elbow_joint" value="{}" />\n\
        <joint name="ur5_wrist_1_joint" value="{}" />\n\
        <joint name="ur5_wrist_2_joint" value="{}" />\n\
        <joint name="ur5_wrist_3_joint" value="{}" />\n\
	</group_state>\n'.format(*([i]+js))
	print(s)